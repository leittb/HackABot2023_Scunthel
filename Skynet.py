from http import server
from turtle import towards
import serial
import math
import time
import requests
import re

server = "http://192.168.4.1"
#server = "http://localhost:8080"
nano = serial.Serial(port='/dev/cu.usbserial-141440', baudrate=9600, timeout=.01)

# enviroment variables
ourGoal, oppGoal, opponents = [],[],[]
oldPos = [[[],0],[[],0]]
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
    print("BYTES :", bytes(message, 'utf-8'))
    print("RESULT : ", nano.readline())

# finds out whose goal is whose
def get_goals():
    while(True):
        try:
            environmentDict = get_loc(server)
            M8coords = environmentDict["M8"]

            G42coords = environmentDict["G42"]
            G43coords = environmentDict["G43"]

            euclid42 = euclidean_distance(M8coords, G42coords)
            euclid43 = euclidean_distance(M8coords, G43coords)

            #chooses our goal
            print("PASS: Successfuly found both goals")
            if euclid42 > euclid43:
                return environmentDict["G43"], environmentDict["G42"]
            else:
                return environmentDict["G42"], environmentDict["G43"]
        except:
            print("FAIL: Failed to initilazie goals, trying again")
            time.sleep(0.2)
        
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
        if bot.startswith('M'):
            left = 200
            right = 90
            bottom = 40
            top = 100
            ball_x = dict['B'][0]
            ball_y = dict['B'][1]
            dude_x = metric[0]
            dude_y = metric[1]
            rotation = 2 * math.pi - metric[2]
            new_a_us_x = 0 - top * math.sin(rotation) + dude_x
            new_a_us_y = 0 + top * math.cos(rotation) + dude_y
            new_c_us_x = -left * math.cos(rotation) + dude_x
            new_c_us_y = -left * math.sin(rotation) + dude_y
            new_a_em_x = right * math.cos(rotation) - top * math.sin(rotation) + dude_x
            new_a_em_y = right * math.sin(rotation) - top * math.cos(rotation) + dude_y
            new_b_em_x = right * math.cos(rotation) - -bottom * math.sin(rotation) + dude_x
            new_b_em_y = right * math.sin(rotation) - -bottom * math.cos(rotation) + dude_y
            new_c_em_x = -left * math.cos(rotation) - -bottom * math.sin(rotation) + dude_x
            new_c_em_y = -left * math.sin(rotation) - -bottom * math.cos(rotation) + dude_y
            if bot == 'M7':
                if 0 <= (dude_x - new_a_us_x)*(ball_x - new_a_us_x) + (dude_y - new_a_us_y)*(ball_y - new_a_us_y) <= (dude_x - new_a_us_x)*(dude_x - new_a_us_x) + (dude_y - new_a_us_y)*(dude_y - new_a_us_y) and 0 <= (new_c_us_x - dude_x)*(ball_x - dude_x) + (new_c_us_y - dude_y)*(ball_y - dude_y) <= (new_c_us_x - dude_x)*(new_c_us_x - dude_x) + (new_c_us_y - dude_y)*(new_c_us_y - dude_y):
                    return 1
            else:
                if 0 <= (new_b_em_x - new_a_em_x)*(ball_x - new_a_em_x) + (new_b_em_y - new_a_em_y)*(ball_y - new_a_em_y) <= (new_b_em_x - new_a_em_x)*(new_b_em_x - new_a_em_x) + (new_b_em_y - new_a_em_y)*(new_b_em_y + new_a_em_y) and 0 <= (new_c_em_x - new_b_em_x)*(ball_x - new_b_em_x) + (new_c_em_y - new_b_em_y)*(ball_y - new_b_em_y) <= (new_c_em_x - new_b_em_x)*(new_c_em_x - new_b_em_x) + (new_c_em_y - new_b_em_y)*(new_c_em_y - new_b_em_y):
                    return 0
    return 2

# Function to check if ball is in front of car
def isInFront(botCoords,BallCoords):
    angle = math.atan2(botCoords[1]-BallCoords[1],botCoords[0]-BallCoords[0])
    angle_diff = botCoords[2] - angle
    angleTol = 0.15
    if abs(angle_diff)<angleTol and euclidean_distance(botCoords,BallCoords)<130:
        return True
    return False
        
# move the robot toward the ball
def move_towards(mona_id, mona_loc, target_loc):
    angle = math.atan2(mona_loc[1]-target_loc[1],mona_loc[0]-target_loc[0])
    angle_diff = mona_loc[2] - angle
    if angle_diff > math.pi:
        angle_diff = math.pi - angle_diff
    if angle_diff < -math.pi:
        angle_diff = -math.pi - angle_diff
    tol = 0.15
    print(mona_loc, target_loc, mona_loc[2], angle, angle_diff)
    if (angle_diff > tol):
        print("----RIGHT-----")
        move_bot(mona_id,0,90)
    elif (angle_diff < -tol):
        print("----LEFT-----")
        move_bot(mona_id,90,0)
    else:
        print("----ONWARD-----")
        move_bot(mona_id,60,60)

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
    ourGoal, oppGoal = get_goals()
    opponents = get_opponents(init_locations)

# START of program
init()

# main execution loop
while True:

    time.sleep(0.1)

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
        if oldPos[0][0] == mona_7:
            oldPos[0][1]+=1
        else:
            oldPos[0][0] = mona_7
        if oldPos[0][1] > 10 and oldPos[0][1] < 20:
            oldPos[0][1]+=1
            move_bot(7,-120,-120)
        elif oldPos[0][1] > 20:
            oldPos[0][1]=0
        else:
            eneny_1 = locations[opponents[0]]
            eneny_2 = locations[opponents[1]]
            target = eneny_1 if euclidean_distance(mona_7, eneny_1) < euclidean_distance(mona_7, eneny_2) else eneny_2
            move_towards(7,mona_7,target)
    except:
        print("FAIL: Unamble to calculate MONA 7 movement")

    time.sleep(0.1)                                                                                                                                                                                                                                     
    # logic for MONA 8 "the grabber"
    try:
        mona_8 = locations['M8']
        if isInFront(mona_8,ball):
            print("GOING FPR GOAL")
            move_towards(8,mona_8,oppGoal)
        if oldPos[1][0] == mona_8:
            oldPos[1][1]+=1
        else:
            oldPos[1][0] = mona_8
        if oldPos[1][1] > 10 and oldPos[1][1] < 20:
            oldPos[1][1]+=1
            move_bot(8,-120,-120)
        elif oldPos[1][1] > 20:
            oldPos[1][1]=0
        else:
            if isInFront(mona_8,ball):
                move_towards(8,mona_8,oppGoal)
            else:
                move_towards(8,mona_8,ball)
        #keyboard_control()
    except:
        print("FAIL: Unamble to calculate MONA 8 movement")

    