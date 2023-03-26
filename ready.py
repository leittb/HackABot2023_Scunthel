# Importing Libraries
import serial
import time
arduino = serial.Serial(port='COM7', baudrate=115200, timeout=.1)
def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return data

while True:
    if arduino.in_waiting:
        data = arduino.readline()
        print(data) # printing the value
    time.sleep(0.5)
    #value = write_read(num)
    
