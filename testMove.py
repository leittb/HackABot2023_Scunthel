import codeyModule as cm
import time
import serial

arduino = serial.Serial(port='/dev/cu.usbserial-141440', baudrate=115200, timeout=0)

while(True):
    key = input()
    if key == 'w' : cm.move_bot(8,100,100)
    if key == 's' : cm.move_bot(8,-100,-100)
    if key == 'q' : cm.move_bot(8,0,0)
    time.sleep(0.1)


# while True:
#     arduino.write("811100100\n".encode())
#     val = arduino.readline().decode("utf-8")
#     if (val != ''):
#         print(val)
#     time.sleep(1)
#     arduino.write("800000000\n".encode())
#     val = arduino.readline().decode("utf-8")
#     if (val != ''):
#         print(val)
#     time.sleep(1)