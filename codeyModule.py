# Importing Libraries
import serial
import time
arduino = serial.Serial(port='COM9', baudrate=115200, timeout=.1)

def sendMessage(mess):
    arduino.write(bytes(mess, 'utf-8'))
def customMovement(bot,Lmot,Rmot):
    ld = "0"
    rd = "0"
    if Lmot > 0:
        ld="1"
    if Rmot > 0:
        rd="1"
    sendMessage(str(bot)+str(ld)+str(rd)+str(Lmot).zfill(3)+str(Rmot).zfill(3))
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