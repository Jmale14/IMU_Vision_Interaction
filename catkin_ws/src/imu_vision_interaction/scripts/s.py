#!/usr/bin/env python3

import subprocess
import shlex
import bluetooth
import time

target_address = None
ID = 'F2:C7:80'
quit = False
connected = False

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
        # self._connected = True
        #status = subprocess.call("bluetooth-agent " + '1234' + " &", shell=True)
        process = subprocess.Popen(f"sudo rfcomm connect -i {target_address} 1 > out.txt", shell=True)#, stdout=subprocess.PIPE)
        print(process.poll())
        print('Connecting...')
        while True:
            f = open("out.txt", "r")
            print(f"out.txt: {f.read()}")

            time.sleep(0.5)
            if process.poll() is not None:
                print(process.poll())
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

