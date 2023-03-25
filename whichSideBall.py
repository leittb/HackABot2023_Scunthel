import math
#true our side false their side
def whichSideIsBall(environmentDict,ourGoal):
    Bcoords = environmentDict["B"]
    ourGoalCoords = environmentDict[ourGoal]
    if ourGoal == "G43":
        theirGoalCoords = environmentDict["G42"]
    else:
        theirGoalCoords = environmentDict["G43"]

    xdistOur = abs(Bcoords[0] - ourGoalCoords[0])
    ydistOur = abs(Bcoords[1] - ourGoalCoords[1])

    xdistTheir = abs(Bcoords[0] - theirGoalCoords[0])
    ydistTheir = abs(Bcoords[1] - theirGoalCoords[1])

    #calcs closer goal
    euclidOur = math.sqrt( (xdistOur**2) + (ydistOur**2) )
    euclidTheir = math.sqrt( (xdistTheir**2) + (ydistTheir**2) )

    #chooses our goal
    if euclidOur > euclidTheir:
        theSide = True
    else:
        theSide = False

    return theSide
