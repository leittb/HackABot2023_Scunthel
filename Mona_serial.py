# Importing Libraries
import serial
import time
mona = serial.Serial(port='/dev/cu.usbserial-DN05JRND', baudrate=115200, timeout=.1)
while True:
    time.sleep(0.05)
    mona_val = mona.readline().decode("utf-8") 
    if (mona_val != ''):
        print(mona_val)
