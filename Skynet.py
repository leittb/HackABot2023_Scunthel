from http import server
from turtle import towards
import serial
import math
import time
import requests
import re

server = "http://192.168.4.1"
#server = "http://localhost:8080"
nano = serial.Serial(port='/dev/cu.usbserial-141440', baudrate=115200, timeout=.01)

# enviroment variables
ourGoal, oppGoal, opponents = "","",[]

# euclidiean distance
def euclidean_distance(l1, l2):
    return math.sqrt((l2[0] - l1[0])**2 + (l2[1] - l1[1])**2)

# gets the locations of the objects
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

# moves the robot
def move_bot(bot,Lmot,Rmot):
    ld = "1" if Lmot > 0 else "0"
    rd = "1" if Rmot > 0 else "0"
    message = str(bot)+str(ld)+str(rd)+str(abs(Lmot)).zfill(3)+str(abs(Rmot)).zfill(3)+'\n'
    nano.write(bytes(message, 'utf-8'))

# finds out whose goal is whose
def get_goals(environmentDict):
    try:
        M8coords = environmentDict["M8"]

        G42coords = environmentDict["G42"]
        G43coords = environmentDict["G43"]

        euclid42 = euclidean_distance(M8coords, G42coords)
        euclid43 = euclidean_distance(M8coords, G43coords)

        #chooses our goal
        print("PASS: Successfuly found both goals")
        if euclid42 > euclid43:
            return "G43", "G42"
        else:
            return "G42", 'G43'
    except:
        print("FAIL: Failed to initilazie goals")
        return "",""
        
# finds the tags of the opposing robots
def get_opponents(environmentDict):
    try:
        keys = environmentDict.keys()
        mona_re = re.compile("M([0-6]|9)|[0-9][0-9]")
        opponet_monas = list(filter(mona_re.match, keys))
        if (len(opponet_monas) == 2):
            print("PASS: Successfuly found opponent Monas")
        else:
            print("FAIL: Failed to find opponents")
        return opponet_monas
    except:
        print("FAIL: Failed to find opponents")

# keyboard control for testing
def keyboard_control():
    key = input()
    if key == 'w' : move_bot(8,100,100)
    if key == 's' : move_bot(8,-100,-100)
    if key == 'a' : move_bot(8,-100,100)
    if key == 'd' : move_bot(8,100,-100)
    if key == 'q' : move_bot(8,0,0)

# Function to check who has possession. Any iterals in the conditional statements will need to be tweaked for better constraints
# Returns 0 if other team has possession, 1 if we have possession, 2 if no one has possession
def who_has_possession(dict):
    for (bot, metric) in dict.items():
        ball_x = dict['B'][0]
        ball_y = dict['B'][1]
        dude_x = metric[0]
        dude_y = metric[1]
        if bot == 'M7':
            if ball_x < dude_x and ball_x > dude_x - 200 and ball_y < dude_y + 100 and ball_y > dude_y - 40:
                return 1
        else:
            if ball_x < dude_x + 90 and ball_x > dude_x - 200 and ball_y < dude_y + 100 and ball_y > dude_y - 40:
                return 0
    return 2
# Function to check if ball is in front of car
def isInFront(botCoords,BallCoords):
    angle = math.atan((BallCoords[1]-botCoords[1])/(BallCoords[0]-botCoords[0]))
    angle_diff = botCoords[2] - angle
    angleTol = 0.1
    if abs(angle_diff)<angleTol and euclidean_distance(botCoords,BallCoords)<100:
        return True
    return False
        
# move the robot toward the ball
def move_towards(mona_id, mona_loc, target_loc):
    angle = math.atan((target_loc[1]-mona_loc[1])/(target_loc[0]-mona_loc[0]))
    angle_diff = mona_loc[2] - angle
    tol = 0.1
    if (angle_diff > tol):
        move_bot(mona_id,120-(120*abs(angle_diff)/math.pi),120)
    elif (angle_diff < -tol):
        move_bot(mona_id,120,120-(120*abs(angle_diff)/math.pi))
    else:
        move_bot(mona_id,120,120)

# says wheather a mona is next to a object TODO
def next_to(mona_loc, target_loc):
    ...

# says wheather a mona is at a target location
def at(mona_loc, target_loc):
    tolerance = 15
    return euclidean_distance(mona_loc, target_loc) <= tolerance

#initializes variables
def init():
    global ourGoal, oppGoal, opponents
    init_locations = get_loc(server)
    ourGoal, oppGoal = get_goals(init_locations)
    opponents = get_opponents(init_locations)

# START of program
init()

# main execution loop
while True:

    time.sleep(0.05)

    locations = get_loc(server)

    # finding the ball
    try:
        ball = locations['B']
    except:
        print("Unable to find ball, skipping evaluation")
        break

    # logic for MONA 7 "The wedge"
    try:
        mona_7 = locations['M7']
        eneny_1 = locations[opponents[0]]
        eneny_2 = locations[opponents[1]]
        target = eneny_1 if euclidean_distance(mona_7, eneny_1) < euclidean_distance(mona_7, eneny_2) else eneny_2
        move_towards(7,mona_7,target)
    except:
        print("FAIL: Unamble to calculate MONA 7 movement")
                                                                                                                                                                                                                                               
    # logic for MONA 8 "the grabber"
    try:
        mona_8 = locations['M8']
        move_towards(8,mona_8,ball)
        #keyboard_control()
    except:
        print("FAIL: Unamble to calculate MONA 8 movement")

    