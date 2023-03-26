# Importing Libraries
import serial
import time
arduino = serial.Serial(port='/dev/cu.usbserial-141440', baudrate=115200, timeout=.01)
    
def move_bot(bot,Lmot,Rmot):
    print("moving")
    ld = "0"
    rd = "0"
    if Lmot > 0:
        ld="1"
    if Rmot > 0:
        rd="1"
    message = str(bot)+str(ld)+str(rd)+str(abs(Lmot)).zfill(3)+str(abs(Rmot)).zfill(3)+'\n'
    arduino.write(bytes(message, 'utf-8'))
