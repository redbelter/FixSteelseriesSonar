from steelseries_sonar_py import Sonar
import sys
import pywinusb.hid as hid
import datetime
import time


def setsonarstuff():
    print("start")
    sonar = Sonar()
    volume_data = sonar.get_volume_data()
    print("Volume Data:", volume_data)
    time.sleep(10)
    print("sleep done")

    #this fixes devices that got fucked up
    sonar.set_streamer_mode(True)
    sonar.set_streamer_mode(False)
    volume_data = sonar.get_volume_data()
    print("Volume Data:", volume_data)
    print("stop")


#loop forever waiting for a usb device you care about to change
def watchForChanges():
    all_hids = hid.find_all_hid_devices()
    found = False
    prevResult = False
    while True:
        found = False
        for device in all_hids:
            # Extract relevant information from the device and add it to the devices list
            #Change this to whatever device you want to trigger it on
            if(device.product_name == "HyperX QuadCast S"):
                #print("found it")
                if(device.is_plugged()):
                    found = True
                else:
                    found = False
        
        if(found and not prevResult):
            prevResult = True
            print("it came back")
            setsonarstuff()
        if(not found and prevResult):
            prevResult = False
            print("its gone")

        #print(str(datetime.datetime.now())+" found: " + str(found) + " and prevResult: " + str(prevResult))
        time.sleep(5)


watchForChanges()