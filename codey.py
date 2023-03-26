# Importing Libraries
import serial
import time
arduino = serial.Serial(port='COM9', baudrate=115200, timeout=.1)
def write_read(x):
    arduino.write(x.to_bytes(2, 'big'))
    time.sleep(5)
    data = arduino.readline()
    return data
while True:
    letter = input("Enter either W or S: ") # Taking input from user
    #arduino.write(bytes(letter, 'utf-8'))
    
    value = write_read(int(letter))
    print(value) # printing the value
    #data = arduino.readline()
    #print(data)
