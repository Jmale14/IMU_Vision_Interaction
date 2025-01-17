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
from std_msgs.msg import Int8, Float64
import socket
import io
import shlex
from imu_classifier import classify_data
from imu_vision_interaction.msg import IMU_msg

# Argument parsing
parser = argparse.ArgumentParser(
    description='Base structure for connecting and streaming data from Shimmer 3 IMU sensor')

parser.add_argument('--disp', '-V',
                    help='Enable displaying of live graphs',
                    default=False,
                    action="store_true")

parser.add_argument('--classify', '-C',
                    help='Classify data',
                    default=None,
                    action="store_true")

parser.add_argument('--bar', '-B',
                    help='Enable displaying of live prediction bar plot',
                    default=False,
                    action="store_true")

args = parser.parse_args()

serialports = ['/dev/rfcomm0', '/dev/rfcomm1', '/dev/rfcomm2']
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
quit_IMU = False
passkey = "1234"  # passkey of shimmers
pos = np.arange(len(CATEGORIES))

if args.disp:
    plt.ion()
    fig, axs = plt.subplots(numsensors, 2)


def shutdown_imu():
    global quit_IMU
    quit_IMU = True


def plot_func(plotdata):
    if not quit_IMU:
        if numsensors == 1:
            for j in range(0, 2):
                axs[j].cla()
                axs[j].plot(plotdata[:, (j*3)])
                axs[j].plot(plotdata[:, (j*3)+1])
                axs[j].plot(plotdata[:, (j*3)+2])
                plt.gca()
                if j == 0:
                    axs[j].set_ylim([-25, 25])
                    axs[j].set_ylabel(f"m/s^2")
                    axs[j].set_title(f"{POSITIONS[0]} Sensor Accelerometer")
                else:
                    axs[j].set_ylim([-500, 500])
                    axs[j].set_ylabel(f"Deg/s")
                    axs[j].set_title(f"{POSITIONS[0]} Sensor Gyroscope")
        else:
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
        self._num = q
        self._ddata = b''
        self._batt_time = time.time()
        self._numbytes = 0
        self._batt_arr = np.empty((1, 0))
        self._shutdown = True
        self._status = 4
        rospy.on_shutdown(self.shutdown)

    def wait_for_ack(self):
        ddata = b''
        ack = struct.pack('B', 0xff)
        count = 0
        timer = time.time()
        while ddata != ack:
            if time.time() - timer < 1:
                try:
                    ddata = self._serial.read(1)
                except Exception as e:
                    print(f"Error reading acknowledgment from {self._location} sensor: {e}")
                    self._connected = False
                    count = count + 1
                if count > 3:
                    print(f"###---{self._location} acknowledgement error---###")
                    return False
            #print("0x%02x" % ord(ddata))
            else:
                print(f"###---{self._location} acknowledgement timeout---###")
                return False
        return True

    def initiate(self):
        while (not self._connected) & (not self._connect_error) & (not quit_IMU):
            time.sleep(5)
            try:
                self._serial = serial.Serial(self._port, 115200, timeout=5)
                self._serial.flushInput()
                print(f"---{self._location} port opening, done.")
                # send the set sensors command
                self._serial.write(struct.pack('BBBB', 0x08, 0xC0, 0x20, 0x00))  # analogaccel, mpu gyro, batt volt
                if not self.wait_for_ack():
                    return False
                self._connected = True
                self._status = 6
                print(f"---{self._location} sensor setting, done.")
                # send the set sampling rate command
                self._serial.write(
                    struct.pack('BBB', 0x05, 0x80,
                                0x02))  # 51.2Hz (6400 (0x1900)). Has to be done like this for alignment reasons
                if not self.wait_for_ack():
                    return False
                print(f"---{self._location} sampling rate setting, done.")
                # send start streaming command
                self._serial.write(struct.pack('B', 0x07))
                if not self.wait_for_ack():
                    return False
                print(f"---{self._location} start command sending, done.")
                #self.inquiry_response()  # Use this if you want to find the structure of data that will be streamed back

            except Exception as e:
                print(f'exception in {self._location} initiate: {e}')
                self._connected = False
        return True

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
        while (numbytes < framesize) and (not quit_IMU):
            ddata = ddata + self._serial.read(framesize)
            print(ddata)
            numbytes = len(ddata)

        data = ddata[0:framesize]
        ddata = ddata[framesize:]
        #numbytes = len(ddata)
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

    def bt_connection(self):
        count = 1
        self._status = 5
        while self._connect_error & (not quit_IMU) & (count <= 3):
            print(f"Trying to connect {self._location}, attempt {count}/3")
            target_address = None
            try:
                print(f"Finding Devices for {self._location}...")
                nearby_devices = bluetooth.discover_devices()
                for bdaddr in nearby_devices:
                    if self._ID == bdaddr[-8:]:
                        target_address = bdaddr
                        break
            except bluetooth.btcommon.BluetoothError as e:
                print(f"Discover Devices error: {e}")

            if target_address is not None:
                print(f"found {self._location} bluetooth device with address {target_address}")

                # Start a new "bluetooth-agent" process where XXXX is the passkey
                #subprocess.call(f"bluetooth-agent {passkey}", shell=True)

                try:
                    self._connection = subprocess.Popen(f"sudo rfcomm connect {self._port} {target_address} 1", shell=True)
                    time.sleep(1)
                    self._connect_error = False
                    return True

                except Exception as e:
                    self._connect_error = True
                    self._connected = False
                    print(f"Exception in connecting {self._location}: {e}")
                    exc_type, exc_obj, exc_tb = sys.exc_info()
                    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                    print(exc_type, fname, exc_tb.tb_lineno)

            else:
                print(f"could not find {self._location} bluetooth device nearby")
                self._connect_error = True
                self._connected = False
            count = count + 1

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
        elif self._batt < 3.8034:
            self._batt_perc = 53.1
        elif self._batt < 3.8106:
            self._batt_perc = 57.0
        elif self._batt < 3.8394:
            self._batt_perc = 61.0
        elif self._batt < 3.861:
            self._batt_perc = 64.9
        elif self._batt < 3.8826:
            self._batt_perc = 68.9
        elif self._batt < 3.9078:
            self._batt_perc = 72.8
        elif self._batt < 3.933:
            self._batt_perc = 76.7
        elif self._batt < 3.969:
            self._batt_perc = 80.7
        elif self._batt < 4.0086:
            self._batt_perc = 84.6
        elif self._batt < 4.041:
            self._batt_perc = 88.5
        elif self._batt < 4.0734:
            self._batt_perc = 92.5
        elif self._batt < 4.113:
            self._batt_perc = 96.4
        else:
            self._batt_perc = 100

        if (self._batt_perc != batt_last) & (self._batt_perc is not None):
            print(f"{self._location} sensor battery at {self._batt_perc}%")

    def start(self):
        # Start thread for shimmer connection
        # connect_threads[num] = threading.Thread(target=shimmers[num].bt_connection, args=(num,))
        # connect_threads[num].start()
        if self.bt_connection():
            if self.initiate():  # Send set up commands, etc to shimmer
                print(f'---Initiated {self._location} Sensor---')
                return True
            else:
                print(f"Failed to initialise {self._location} sensor")
                return False
        else:
            print(f"Failed to connect {self._location} sensor")
            return False

    def getdata(self):
        framesize = 18  # 1byte packet type + 3byte timestamp + 3x2byte Analog Accel + 2byte Battery + 3x2byte Gyro
        while self._numbytes < framesize and (not quit_IMU):
            try:
                self._ddata = self._ddata + self._serial.read(framesize)
            except Exception as e:
                print(f"Unable to read {self._location} IMU data, {e}")
            self._numbytes = len(self._ddata)

        data = self._ddata[0:framesize]
        self._ddata = self._ddata[framesize:]
        self._numbytes = len(self._ddata)

        accel = self.calibrate_data(np.array(struct.unpack('HHH', data[4:10]), ndmin=2), 'a')
        self._accel = np.vstack((self._accel, accel))
        self._accel = self._accel[-WIN_LEN:, :]
        self._accel = np.nan_to_num(self._accel)

        batt_now = struct.unpack('H', data[10:12])[0] * 6 / 4095
        batt_now = np.nan_to_num(batt_now)
        self._batt_arr = np.append(self._batt_arr, batt_now)
        self._batt = np.mean(self._batt_arr)
        while len(self._batt_arr) > 50:
            self._batt_arr = np.delete(self._batt_arr, 0)

        if (time.time() - self._batt_time) > 1:
            self.checkbattery()
            self._batt_time = time.time()

        gyro = self.calibrate_data(np.array(struct.unpack('>hhh', data[12:framesize]), ndmin=2), 'g')
        self._gyro = np.vstack((self._gyro, gyro))
        self._gyro = self._gyro[-WIN_LEN:, :]
        self._gyro = np.nan_to_num(self._gyro)
        self._status = 1
        return True

    def shutdown(self):
        # Reset all flags/parameters
        self._connected = False
        self._connection = None
        self._ready = False
        self._connect_error = True

        # Shut sensor down and kill serial connection
        try:
            # send stop streaming command
            self._serial.write(struct.pack('B', 0x20))
            print(f"{self._location} stop command sent, waiting for ACK_COMMAND")
            if self.wait_for_ack():
                print(f"---{self._location} stop ACK_COMMAND received.")
                # close serial port
                self._serial.close()
            else:
                print(f"---{self._location} stop ACK_COMMAND *NOT* received.")
        except Exception:
            pass

        #Kill bluetooth connection
        try:
            self._connection.release()
            self._connection.kill()
        except Exception:
            pass

        return True

def shimmer_thread(num):
    print(f"Setting up Sensor {num + 1}/{numsensors}")
    shimmers[num] = shimmer(num)  # Create instance of shimmer class for each device

    # read incoming data
    first_try = True
    while not quit_IMU:
        if shimmers[num]._ready and (not quit_IMU):
            if shimmers[num]._connected:
                success = shimmers[num].getdata()
            else:
                print(f"{shimmers[num]._location} not connected?")

        elif not quit_IMU:
            if first_try:
                # Try starting connection
                print(f"Starting {POSITIONS[num]} connection and initialisation")
                first_try = False
            else:
                # Try restarting connection
                print(f"Lost {POSITIONS[num]} connection, restarting")

            shimmers[num]._shutdown = False
            shimmers[num]._ready = shimmers[num].start()

            if shimmers[num]._ready:
                print(f"{shimmers[num]._location} sensor connected, starting data stream {num + 1}")
            else:
                print(f"{shimmers[num]._location} sensor failed to start successfully, retrying")
                shimmers[num]._shutdown = shimmers[num].shutdown()

    # quit_IMU condition
    #shutdown = shimmers[num].shutdown()



def IMUsensorsMain():
    print("-----Here we go-----")
    pub = rospy.Publisher('IMU_Data', IMU_msg, queue_size=1)
    rospy.init_node('shimmerBase', anonymous=True)
    rate = rospy.Rate(2)  # Message publication rate, Hz => should be 2
    prediction = np.zeros(5)


    # Start separate thread for collecting data from each Shimmer
    for shimthread in range(0, numsensors):
        shim_threads[shimthread] = threading.Thread(target=shimmer_thread, args=(shimthread,))
        shim_threads[shimthread].start()

    ready = np.zeros((len(shim_threads)))  # Bool array for if shimmers are setup and streaming
    alive = np.zeros((len(shim_threads)))  # Bool array for if shimmer thread are active
    conn = np.zeros((len(shim_threads)))  # Bool array for if connections are successful
    s_down = np.zeros((len(shim_threads)))  # Bool array for if sensors are shutdown
    time.sleep(1)

    print("Starting main loop")
    msg = IMU_msg()
    class_pred = CATEGORIES[-1]
    status = [2, 2, 2, 2]

    while not quit_IMU:
        status[3] = 2
        for s in shimmers:
            ready[s] = shimmers[s]._ready
            alive[s] = shim_threads[s].isAlive()
            conn[s] = shimmers[s]._connected
            s_down[s] = shimmers[s]._shutdown
            status[s] = shimmers[s]._status
        out_str = f"Sensors Ready:{ready} Threads:{alive} Connections:{conn} Shutdowns:{s_down} " \
                  f"Total Threads:{threading.active_count()} Quit:{quit_IMU} Prediction:{class_pred}"
        #out_str = threading.enumerate()
        print(out_str)
        class_pred = CATEGORIES[-1]
        new_data = np.empty((WIN_LEN, 0), dtype=np.float64)
        if all(ready) & all(conn) & all(alive):
            for p in shimmers:
                new_data = np.hstack((new_data, shimmers[p]._accel, shimmers[p]._gyro))
            new_data = np.nan_to_num(new_data)
            scaler = preprocessing.StandardScaler()
            # for i in range(0, X.shape[0]):
            #     scaler = preprocessing.StandardScaler()
            #     X[i, :, :] = scaler.fit_transform(X[i, :, :])
            new_data[:, :] = scaler.fit_transform(new_data[:, :])
            status[3] = 1

            if args.classify:
                prediction = classify_data(new_data, args.bar)
                prediction = np.reshape(prediction, (-1))
                class_pred = CATEGORIES[np.argmax(prediction)]

        if all(ready) & all(conn) & all(alive) & (not quit_IMU) & args.disp:
            plotdata = np.empty((WIN_LEN, 0), dtype=np.float64)
            for p in shimmers:
                plotdata = np.hstack((plotdata, shimmers[p]._accel, shimmers[p]._gyro))
            plotdata = np.nan_to_num(plotdata)
            plot_func(plotdata)

        #rospy.loginfo(out_str)
        msg.imu_msg = prediction.tolist()
        msg.imu_stat = status
        pub.publish(msg)
        rate.sleep()


if __name__ == "__main__":
    subprocess.call("sudo rfcomm release all", shell=True)
    # kill any rfcomm connections currently active
    subprocess.call("sudo killall rfcomm", shell=True)
    # kill any "bluetooth-agent" process that is already running
    #subprocess.call("kill -9 `pidof bluetooth-agent`", shell=True)
    rospy.on_shutdown(shutdown_imu)
    try:
        IMUsensorsMain()
    except rospy.ROSInterruptException:
        quit_IMU = True
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
        quit_IMU = True
        subprocess.call("sudo rfcomm release all", shell=True)

        ready = np.zeros((len(shim_threads)))  # Bool array for if shimmers are setup and streaming
        alive = np.zeros((len(shim_threads)))  # Bool array for if shimmer thread are active
        conn = np.zeros((len(shim_threads)))  # Bool array for if connections are successful
        s_down = np.zeros((len(shim_threads)))  # Bool array for if sensors are shutdown

        for s in shimmers:
            ready[s] = shimmers[s]._ready
            alive[s] = shim_threads[s].isAlive()
            conn[s] = shimmers[s]._connected
            s_down[s] = shimmers[s]._shutdown

        print("###---End Status---###")
        print(f"Sensors Ready:{ready} Threads:{alive} Connections:{conn} Shutdowns:{s_down} "
              f"Threads:{threading.active_count()} Quit:{quit_IMU}")

        print("All done")
