#!/usr/bin/env python3

import subprocess
import shlex
import bluetooth
import time
import threading

target_address = None
ID = 'F2:C7:80'
quit = False
connected = False
process = [None] * 1
subprocess.run("sudo rfcomm release all", shell=True)
subprocess.run("sudo killall rfcomm", shell=True)
# kill any "bluetooth-agent" process that is already running
subprocess.run("kill -9 `pidof bluetooth-agent`", shell=True)


try:
    nearby_devices = bluetooth.discover_devices()
except bluetooth.btcommon.BluetoothError as e:
    print(f"Discover Devices error: {e}")

for bdaddr in nearby_devices:
    if ID == bdaddr[-8:]:
        target_address = bdaddr
        break

if target_address is not None:
    print(f"found bluetooth device with address {target_address}")

    try:
        #status = subprocess.call("bluetooth-agent " + '1234' + " &", shell=True)

        process[0] = subprocess.Popen(f"sudo rfcomm connect -i {target_address} 1", shell=True)

        time.sleep(5)
        print(process[0].poll())
        print('Connecting...')
        while True:
            #f = open("out.txt", "r")
            #print(f"out.txt: {f.read()}")
            print(process[0].poll())#, thread1.is_alive())
            time.sleep(0.5)
            subprocess.call("sudo killall rfcomm", shell=True)
            print(process[0].poll())  # , thread1.is_alive())
            time.sleep(0.5)
            subprocess.Popen("sudo rfcomm release all", shell=True)
            print(process[0].poll())  # , thread1.is_alive())
            time.sleep(0.5)
            process[0].kill()
            print(process[0].poll())  # , thread1.is_alive())
            time.sleep(0.5)
            if process[0].poll() is not None:
                pass
            # try:
            #     output = process.stdout.read()
            # except Exception as e:
            #     print(e)
            #     pass
            # print(f"{output}   {process.poll()}")
            # if output == '' and process.poll() is not None:
            #     break
            # if output:
            #     print(output.strip())

        print(f"Quitting from connection thread")
        quit = True

    except Exception as e:
        print(f"Caught exception in connecting : {e}")
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)
        connected = False

    print("Past connection point")

else:
    print(f"could not find {self._location} bluetooth device nearby")
    connected = False



 #   rc = process.poll()
#    return rc

