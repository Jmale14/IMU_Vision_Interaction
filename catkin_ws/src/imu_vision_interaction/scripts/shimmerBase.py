#!/usr/bin/env python3

import sys, struct, serial, os
import numpy as np
import argparse
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time
from sklearn import preprocessing
import bluetooth
from serial.tools import list_ports
import threading
import glob
import signal
import subprocess
import rospy
from std_msgs.msg import String
import socket
import io
import shlex

# Argument parsing
parser = argparse.ArgumentParser(
    description='Base structure for connecting and streaming data from Shimmer 3 IMU sensor')

parser.add_argument('--disp', '-V',
                    help='Enable displaying of live graphs',
                    default=None,
                    action="store_true")

args = parser.parse_args()

serialports = ['/dev/rfcomm0']#, '/dev/rfcomm1', '/dev/rfcomm2']
POSITIONS = ['Hand', 'Wrist', 'ARM']
SHIM_IDs = ['F2:AF:44', 'F2:B6:ED', 'F2:C7:80']
numsensors = len(serialports)

CATEGORIES = ['AllenKeyIn', 'AllenKeyOut', 'ScrewingIn', 'ScrewingOut', 'Null']
Fs = 51.2  # Sampling frequency, Hz
WIN_TIME = 3  # Window length, s
WIN_LEN = round(WIN_TIME * Fs)  # Window length, samples

gyro_offset = [[0], [0], [0]]
gyro_sens = [[65.5, 0, 0], [0, 65.5, 0], [0, 0, 65.5]]
gyro_align = [[0, -1, 0], [-1, 0, 0], [0, 0, -1]]
accel_offset = [[2253], [2253], [2253]]
accel_sens = [[92, 0, 0], [0, 92, 0], [0, 0, 92]]
accel_align = [[0, -1, 0], [-1, 0, 0], [0, 0, -1]]
shimmers = {}
shim_threads = {}
connect_threads = {}
quit = False
passkey = "1234"  # passkey of the device you want to connect
pos = np.arange(len(CATEGORIES))

if args.disp:
    plt.ion()
    fig, axs = plt.subplots(numsensors, 2)

def plot_func(plotdata):
    if not quit:
        for i in range(0, numsensors):
            for j in range(0, 2):
                axs[i, j].cla()
                axs[i, j].plot(plotdata[:, (i*6)+(j*3)])
                axs[i, j].plot(plotdata[:, (i*6)+(j*3)+1])
                axs[i, j].plot(plotdata[:, (i*6)+(j*3)+2])
                plt.gca()
                if j == 0:
                    axs[i, j].set_ylim([-25, 25])
                    axs[i, j].set_ylabel(f"m/s^2")
                    axs[i, j].set_title(f"{POSITIONS[i]} Sensor Accelerometer")
                else:
                    axs[i, j].set_ylim([-500, 500])
                    axs[i, j].set_ylabel(f"Deg/s")
                    axs[i, j].set_title(f"{POSITIONS[i]} Sensor Gyroscope")

        plt.pause(0.0001)


class shimmer():
    def __init__(self, q):
        self._ready = False
        self._connect_error = True
        self._connection = None
        self._connected = False
        self._ID = SHIM_IDs[q]
        self._location = POSITIONS[q]
        self._port = serialports[q]
        self._serial = None
        self._accel = np.zeros((WIN_LEN, 3))
        self._gyro = np.zeros((WIN_LEN, 3))
        self._batt = None
        self._batt_perc = None

    def wait_for_ack(self):
        ddata = b''
        ack = struct.pack('B', 0xff)
        while ddata != ack:
            ddata = self._serial.read(1)
            #print("0x%02x" % ord(ddata))
        return

    def initiate(self, num):
        while (not self._connected) & (not self._connect_error) & (not quit):
            time.sleep(1)
            try:
                self._serial = serial.Serial(self._port, 115200)
                self._serial.flushInput()
                print("  port opening, done.")
                # send the set sensors command
                self._serial.write(struct.pack('BBBB', 0x08, 0xC0, 0x20, 0x00))  # analogaccel, mpu gyro, batt volt
                self.wait_for_ack()
                self._connected = True
                print("  sensor setting, done.")
                # send the set sampling rate command
                self._serial.write(
                    struct.pack('BBB', 0x05, 0x80,
                                0x02))  # 51.2Hz (6400 (0x1900)). Has to be done like this for alignment reasons
                self.wait_for_ack()
                print("  sampling rate setting, done.")
                # send start streaming command
                self._serial.write(struct.pack('B', 0x07))
                self.wait_for_ack()
                print("  start command sending, done.")
                #self.inquiry_response()  # Use this if you want to find the structure of data that will be streamed back

            except Exception as e:
                print(f'exception in initiate: {e}')
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                print(exc_type, fname, exc_tb.tb_lineno)
                self._connected = False

    def inquiry_response(self):
        # Outputs data structure of data to be streamed back
        self._serial.flushInput()
        # send inquiry command
        self._serial.write(struct.pack('B', 0x01))
        self.wait_for_ack()

        # read incoming data
        ddata = b''
        numbytes = 0
        framesize = 9

        print("Inquiry response:")
        while (numbytes < framesize) and (not quit):
            ddata = ddata + self._serial.read(framesize)
            print(ddata)
            numbytes = len(ddata)

        data = ddata[0:framesize]
        ddata = ddata[framesize:]
        numbytes = len(ddata)
        (packettype) = struct.unpack('B', bytes(data[0].to_bytes(1, sys.byteorder)))
        (samplingrate, configByte0, configByte1, configByte2, configByte3, numchans, bufsize) = struct.unpack('HBBBBBB',
                                                                                                              data[1:9])
        print("          Packet type: 0x%02x" % packettype)
        print("        Sampling rate: 0x%04x" % samplingrate)
        print("  Config Setup Byte 0: 0x%02x" % configByte0)
        print("  Config Setup Byte 1: 0x%02x" % configByte1)
        print("  Config Setup Byte 2: 0x%02x" % configByte2)
        print("  Config Setup Byte 3: 0x%02x" % configByte3)
        print("   Number of channels: 0x%02x" % numchans)
        print("          Buffer size: 0x%02x" % bufsize)

        for i in range(numchans):
            data = self._serial.read(1)
            print("           Channel %2d:" % i)
            print("                        0x%02x" % (struct.unpack('B', data[0].to_bytes(1, sys.byteorder))))

        return

    def calibrate_data(self, data, sensor):
        # Calibrate readings to m/s2, deg/s. More info: http://www.shimmersensing.com/images/uploads/docs/Shimmer_9DOF_Calibration_User_Manual_rev2.10a.pdf
        if sensor == 'a':
            Ri = np.linalg.inv(accel_align)
            Ki = np.linalg.inv(accel_sens)
            offset = accel_offset
        elif sensor == 'g':
            Ri = np.linalg.inv(gyro_align)
            Ki = np.linalg.inv(gyro_sens)
            offset = gyro_offset
        else:
            print('Calibration sensor invalid, must be ''a'' or ''g'' ')
            raise ValueError
        calib_data = np.transpose(Ri @ Ki @ (np.transpose(data) - offset))
        return calib_data

    def bt_connection(self, num):
        count = 1
        while self._connect_error & (not quit) & (count <= 3):
            print(f"Trying to connect {self._location}, attempt {count}/3")
            target_address = None
            try:
                print(f"Finding Devices for {self._location}...")
                nearby_devices = bluetooth.discover_devices()
            except bluetooth.btcommon.BluetoothError as e:
                print(f"Discover Devices error: {e}")

            for bdaddr in nearby_devices:
                if self._ID == bdaddr[-8:]:
                    target_address = bdaddr
                    break

            if target_address is not None:
                print(f"found {self._location} bluetooth device with address {target_address}")

                # Start a new "bluetooth-agent" process where XXXX is the passkey
                #subprocess.call(f"bluetooth-agent {passkey}", shell=True)

                try:
                    self._connection = subprocess.Popen(f"sudo rfcomm connect {self._port} {target_address} 1", shell=True)
                    self._connect_error = False
                    return True

                except Exception as e:
                    self._connect_error = True
                    self._connected = False
                    print(f"Caught exception in connecting {self._location}: {e}")
                    exc_type, exc_obj, exc_tb = sys.exc_info()
                    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                    print(exc_type, fname, exc_tb.tb_lineno)

            else:
                print(f"could not find {self._location} bluetooth device nearby, is it turned on?")
                self._connect_error = True
                self._connected = False

        return False

    def checkbattery(self):
        batt_last = self._batt_perc
        if self._batt < 3.2:
            self._batt_perc = 0.0
        elif self._batt < 3.627:
            self._batt_perc = 5.9
        elif self._batt < 3.645:
            self._batt_perc = 9.8
        elif self._batt < 3.663:
            self._batt_perc = 13.8
        elif self._batt < 3.681:
            self._batt_perc = 17.7
        elif self._batt < 3.699:
            self._batt_perc = 21.6
        elif self._batt < 3.717:
            self._batt_perc = 25.6
        elif self._batt < 3.7314:
            self._batt_perc = 29.5
        elif self._batt < 3.735:
            self._batt_perc = 33.4
        elif self._batt < 3.7386:
            self._batt_perc = 37.4
        elif self._batt < 3.7566:
            self._batt_perc = 41.3
        elif self._batt < 3.771:
            self._batt_perc = 45.2
        elif self._batt < 3.789:
            self._batt_perc = 49.2
        else:
            self._batt_perc = 50

        if (self._batt_perc != batt_last) & (self._batt_perc is not None):
            print(f"{self._location} sensor battery at {self._batt_perc}%")

    def start(self, num):
        # Start thread for shimmer connection
        # connect_threads[num] = threading.Thread(target=shimmers[num].bt_connection, args=(num,))
        # connect_threads[num].start()
        if self.bt_connection(num):
            if self.initiate(num):  # Send set up commands, etc to shimmer
                print(f'---Initiated {self._location} Sensor---')
                return True
            else:
                return False
        else:
            return False

    def getdata(self, num, batt_time, ddata, numbytes):
        framesize = 18  # 1byte packet type + 3byte timestamp + 3x2byte Analog Accel + 2byte Battery + 3x2byte Gyro
        while numbytes < framesize and (not quit):
            if time.time() - shim_timeout > 0.5:
                print(f"-----Timeout on sensor {num + 1} - {self._location}-----")
            try:
                ddata = ddata + self._serial.read(framesize)
            except Exception:
                if time.time() - shim_timeout > 0.5:
                    print(f"Unable to read sensor {num + 1} - {self._location}, trying again ")
            numbytes = len(ddata)
            shim_timeout = time.time()

        data = ddata[0:framesize]
        ddata = ddata[framesize:]
        numbytes = len(ddata)

        accel = self.calibrate_data(np.array(struct.unpack('HHH', data[4:10]), ndmin=2), 'a')
        self._accel = np.vstack((self._accel, accel))
        self._accel = self._accel[-WIN_LEN:, :]
        self._accel = np.nan_to_num(self._accel)

        batt_arr = np.empty((1, 0))
        batt_now = struct.unpack('H', data[10:12])[0] * 6 / 4095
        batt_now = np.nan_to_num(batt_now)
        batt_arr = np.append(batt_arr, batt_now)
        self._batt = np.mean(batt_arr)
        if len(batt_arr) == 10:
            batt_arr = np.delete(batt_arr, 0)

        if (time.time() - batt_time) > 1:
            self.checkbattery()
            batt_time = time.time()

        gyro = self.calibrate_data(np.array(struct.unpack('>hhh', data[12:framesize]), ndmin=2), 'g')
        self._gyro = np.vstack((self._gyro, gyro))
        self._gyro = self._gyro[-WIN_LEN:, :]
        self._gyro = np.nan_to_num(self._gyro)
        return batt_time, ddata, numbytes


def shimmer_thread(num):
    print(f"Setting up Sensor {num + 1}/{numsensors}")
    shimmers[num] = shimmer(num)  # Create instance of shimmer class for each device

    # read incoming data
    first_try = True
    batt_time = time.time()
    ddata = b''
    numbytes = 0
    while not quit:
        if shimmers[num]._ready and (not quit):
            if shimmers[num]._connected:
                batt_time, ddata, numbytes = shimmers[num].getdata(num, batt_time, ddata, numbytes)
            else:
                print(f"{shimmers[num]._location} not connected?")

        elif not quit:
            shimmers[num]._connected = False
            shimmers[num]._connection = None
            shimmers[num]._ready = False
            shimmers[num]._connect_error = True
            shimmers[num]._connection.kill()
            if first_try:
                # Try starting connection
                print(f"Starting connection {num + 1} - {POSITIONS[num]}")
                first_try = False
            else:
                # Try restarting connection
                print(f"Lost connection, restarting connection {num+1} - {POSITIONS[num]}")
            shimmers[num]._ready = shimmers[num].start(num)
            print(f"{shimmers[num]._location} sensor connected, starting data stream {num + 1}...")

    # Quit condition
    if shimmers[num]._connected:
        # send stop streaming command
        shimmers[num]._serial.write(struct.pack('B', 0x20))
        print(f"stop command sent for {num}, waiting for ACK_COMMAND")
        shimmers[num].wait_for_ack()
        print("ACK_COMMAND received.")
        # close serial port
        shimmers[num]._serial.close()


def IMUsensorsMain():
    print("-----Here we go-----")
    pub = rospy.Publisher('IMU_Data', String, queue_size=1)
    rospy.init_node('shimmerBase', anonymous=True)
    rate = rospy.Rate(1)

    # Start separate thread for collecting data from each Shimmer
    for shimthread in range(0, numsensors):
        shim_threads[shimthread] = threading.Thread(target=shimmer_thread, args=(shimthread,))
        shim_threads[shimthread].start()

    ready = np.zeros((len(shim_threads)))  # Bool array for if shimmers are setup and streaming
    alive = np.zeros((len(shim_threads)))  # Bool array for if shimmer thread are active
    conn = np.zeros((len(shim_threads)))  # Bool array for if connection threads are active
    time.sleep(1)

    print("Starting main loop")
    while not rospy.is_shutdown():
        print(f"ROSPY: {rospy.is_shutdown()}")
        for s in shimmers:
            ready[s] = shimmers[s]._ready
            alive[s] = shim_threads[s].isAlive()
            conn[s] = shimmers[s]._connected
        out_str = f"Sensors Ready: {ready} Sensor Threads: {alive} Connections: {conn} Total Threads: {threading.active_count()} Quit: {quit}"
        #out_str = threading.enumerate()
        print(out_str)

        new_data = np.empty((WIN_LEN, 0), dtype=np.float64)
        if all(ready) & all(conn) & all(alive):
            for p in shimmers:
                new_data = np.hstack((new_data, shimmers[p]._accel, shimmers[p]._gyro))
            new_data = np.nan_to_num(new_data)
            for i in range(0, new_data.shape[1]):
                new_data[:, i] = preprocessing.scale(new_data[:, i])

            new_data = new_data[np.newaxis, ...]

        # if all(ready) & all(conn) & all(alive) & (not quit) & args.disp:
        #     plotdata = np.empty((WIN_LEN, 0), dtype=np.float64)
        #     for p in shimmers:
        #         plotdata = np.hstack((plotdata, shimmers[p]._accel, shimmers[p]._gyro))
        #     plotdata = np.nan_to_num(plotdata)
        #     plot_func(plotdata)

        #rospy.loginfo(out_str)
        pub.publish(out_str)
        rate.sleep()


if __name__ == "__main__":
    subprocess.call("sudo rfcomm release all", shell=True)
    # kill any rfcomm connections currently active
    subprocess.call("sudo killall rfcomm", shell=True)
    # kill any "bluetooth-agent" process that is already running
    #subprocess.call("kill -9 `pidof bluetooth-agent`", shell=True)

    try:
        IMUsensorsMain()
    except rospy.ROSInterruptException:
        quit = True
        print("Keyboard Interrupt")
        plt.close('all')
    finally:
        threads_alive = True
        while threads_alive:
            threads_alive = False
            for s in shim_threads:
                threads_alive = threads_alive | shim_threads[s].isAlive()
            time.sleep(0.01)

        if args.disp:
            plt.show()
        quit = True
        subprocess.call("sudo rfcomm release all", shell=True)
        for s in shimmers:
            ready[s] = shimmers[s]._ready
            alive[s] = shim_threads[s].isAlive()
            conn[s] = shimmers[s]._connected
        print(f"Shimmers ready: {ready} Threads alive: {alive} Connects alive: {conn}")

        print("All done")
