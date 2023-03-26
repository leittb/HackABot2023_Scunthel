# Importing Libraries
import serial
import time
nano = serial.Serial(port='/dev/cu.usbserial-141440', baudrate=9600, timeout=.1)
while True:
    time.sleep(2)
    nano_val = nano.readline()
    if (nano_val != ''):
        print("NANO : ", nano_val)
