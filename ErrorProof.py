# Importing Libraries
import serial
import time
nano = serial.Serial(port='/dev/cu.usbserial-141440', baudrate=9600, timeout=.1)
mona = serial.Serial(port='/dev/cu.usbserial-DN05JRND', baudrate=115200, timeout=.1)
while True:
    time.sleep(2)
    nano_val = nano.readline()
    mona_val = mona.readline()
    print("NANO : ", nano_val)
    print("MONA : ", mona_val)
