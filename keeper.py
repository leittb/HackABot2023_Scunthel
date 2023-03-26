import math
'''
def intialiseOurGoal(environmentDict):
    M8coords = environmentDict["M8"]

    G42coords = environmentDict["G42"]
    G43coords = environmentDict["G43"]

    xdist42 = abs(M8coords[0] - G42coords[0])
    ydist42 = math.abs(M8coords[1] - G42coords[1])

    xdist43 = math.abs(M8coords[0] - G43coords[0])
    ydist43 = math.abs(M8coords[1] - G43coords[1])

    #calcs closer goal
    euclid42 = math.sqrt( (xdist42**2) + (ydist42**2) )
    euclid43 = math.sqrt( (xdist43**2) + (ydist43**2) )

    #chooses our goal
    if euclid42 > euclid43:
        ourGoal = "G43"
    else:
        ourGoal = "G42"

    return ourGoal
'''
# Define a function to calculate the bearing between two points
def bearing(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    delta_x = x2 - x1
    delta_y = y2 - y1
    radians = math.atan2(delta_y, delta_x)
    degrees = math.degrees(radians)
    return (degrees + 360) % 360



def blockMovement(environmentDict,blockID,ourGoalID):
    blockCoords = environmentDict[blockID]
    ourGoalCoords = environmentDict[ourGoalID]
    ballCoords = environmentDict["B"]

    # Calculate the slope and y-intercept of the line between point1 and point2
    slope = (ourGoalCoords[1] - ballCoords[1]) / (ourGoalCoords[0] - ballCoords[0])
    y_intercept = ballCoords[1] - slope * ballCoords[0]

    # Find the nearest point on the line to point3
    x_nearest = (blockCoords[0] + slope * blockCoords[1] - slope * y_intercept) / (1 + slope**2)
    y_nearest = slope * x_nearest + y_intercept
    point_nearest = (x_nearest, y_nearest)
    print(point_nearest)
    # Calculate the bearing between point3 and point_nearest
    angle = bearing(blockCoords, point_nearest)
    return angle
myDict = {"K":[3,2],"G":[0,0],"B":[7,5]}
print(blockMovement(myDict,"K","G"))
