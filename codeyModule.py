# Importing Libraries
import serial
import time
arduino = serial.Serial(port='COM9', baudrate=115200, timeout=.01)
    
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
def sendMessage(mess):
    arduino.write(bytes(mess, 'utf-8'))
def customMovement(bot,Lmot,Rmot):
    ld = "0"
    rd = "0"
    if Lmot > 0:
        ld="1"
    if Rmot > 0:
        rd="1"
    Lmot= abs(Lmot)
    Rmot= abs(Rmot)
    temp = str(bot)+str(ld)+str(rd)+str(Lmot).zfill(3)+str(Rmot).zfill(3)
    print(temp)
    sendMessage(temp)
def forward(bot,power):
    customMovement(bot,power,power)
def backwards(bot,power):
    customMovement(bot,-power,-power)
def quickRight(bot):
    customMovement(bot,120,-120)
def quickLeft(bot):
    customMovement(bot,-120,120)
def stopMovement(bot):
    customMovement(bot,0,0)