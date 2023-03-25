import math
#true our side false their side
def whichSideIsBall(environmentDict,ourGoal):
    Bcoords = environmentDict["B"]
    ourGoalCoords = environmentDict[ourGoal]
    if ourGoal == "G43":
        theirGoalCoords = environmentDict["G42"]
    else:
        theirGoalCoords = environmentDict["G43"]

    def euclidean_distance(x1, y1, x2, y2):
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    euclidOur = euclidean_distance(Bcoords[0], BCoords[1], ourGoalCoords[0],ourGoalCoords[1])
    euclidTheir = euclidean_distance(Bcoords[0], BCoords[1], theirGoalCoords[0],theirGoalCoords[1])

    #chooses our goal
    if euclidOur > euclidTheir:
        theSide = True
    else:
        theSide = False

    return theSide
