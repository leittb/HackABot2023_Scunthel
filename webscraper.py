
#webscraping
import codeyModule as cm
import math
import time
import requests
import re

#command line args
import sys

#visulaization
from tkinter import *

local_server = "http://localhost:8080"
main_server = "http://192.168.4.1"

if sys.argv[1] == "main":
    server = main_server
elif sys.argv[1] == "local":
    server = local_server

def get_loc(server):
    # get data from the server
    try:
        response = requests.get(server)
        html_content = response.text
        data = [x.strip().split(',') for x in re.findall("[A-Z][0-9]*,[0-9]+,[0-9]+,-?[0-9]\.?[0-9]*",html_content)]
        # get the locations of the items
        locations = {}
        for x in data:
            locations[x[0]] = [float(i) for i in x[1:]]
        
        return locations
    except:
        print("ERROR getting data")
        return {}

starting = True

while (starting):
    try:
        # setup 
        starting = False
    
    except:
        print("starting")

print("start")

while True:

    locations = get_loc(server)

    try:
        ball = locations['B']
        p8 = locations['M8']
        #p7 = locations['M7']

        p8_ang = math.atan((ball[1]-p8[1])/(ball[0]-p8[0]))
        p8_diff = p8[2] - p8_ang
        print(p8_diff)
        tol = 0.1
        if (p8_diff > tol):
            cm.move_bot(8,120-(120*abs(p8_diff)/math.pi),120)
            print("turn left")
        elif (p8_diff < -tol):
            cm.move_bot(8,120,120-(120*abs(p8_diff)/math.pi))
            print("turn right")
        else:
            cm.move_bot(8,120,120)
            print("forward")

    except:
        print("ball error")
        cm.move_bot(8,0,0)

    time.sleep(0.05)

#NOTE tkinter code

window=Tk()
window.title('Fusbol')

window.geometry("1500x1000")

#Create a canvas object
c = Canvas(window,width=1500,height=1000)

locations = get_loc(server)

boundry = 200
x_off = locations['C0'][0] - boundry
y_off = locations['C0'][1] - boundry
scale = 0.5

for k in locations:
    locations[k] = [(locations[k][0]-x_off)*scale, (locations[k][1]-y_off)*scale, locations[k][2]]

c.create_rectangle(locations["C0"][0],locations["C0"][1],locations["C1"][0],locations["C1"][1],outline = "black",fill = "green",width = 1)
c.pack()

r = 20
for i in range(len(locations.values())):
    l = list(locations.values())[i]
    k = list(locations.keys())[i]
    c.create_oval(l[0]-r, l[1]-r, l[0]+r, l[1]+r, outline = "black",fill = "black",width = 2)
    c.create_text(l[0], l[1], text=k, fill="white", font=('Helvetica 15 bold'))
    c.create_line(l[0], l[1], l[0]+math.cos(l[2])*50, l[1]+math.sin(l[2])*50, fill='red')
    c.pack()

window.mainloop()
