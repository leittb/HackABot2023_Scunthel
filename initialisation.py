#dictionary
#key- C1,
#value - 3 element array - x y angle
def intialiseOurGoal(environmentDict):
    M8coords = environmentDict["M8"]

    G42coords = environmentDict["G42"]
    G43coords = environmentDict["G43"]

    xdist42 = Math.abs(M8coords[0] - G42coords[0])
    ydist42 = Math.abs(M8coords[1] - G42coords[1])

    xdist43 = Math.abs(M8coords[0] - G43coords[0])
    ydist43 = Math.abs(M8coords[1] - G43coords[1])

    #calcs closer goal
    euclid42 = math.sqrt( (xdist42**2) + (ydist42**2) )
    euclid43 = math.sqrt( (xdist43**2) + (ydist43**2) )

    #chooses our goal
    if euclid42 > euclid43:
        ourGoal = "G43"
    else:
        ourGoal = "G42"

    return ourGoal
