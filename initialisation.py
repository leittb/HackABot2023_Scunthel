#dictionary
#key- C1,
#value - 3 element array - x y angle
def intialiseOurGoal(environmentDict):
    M8coords = environmentDict["M8"]

    G42coords = environmentDict["G42"]
    G43coords = environmentDict["G43"]

    def euclidean_distance(x1, y1, x2, y2):
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    euclid42 = euclidean_distance(M8coords[0], M8coords[1], G42coords[0], G42coords[1]):
    euclid43 = euclidean_distance(M8coords[0], M8coords[1], G43coords[0], G43coords[1]):

    #chooses our goal
    if euclid42 > euclid43:
        ourGoal = "G43"
    else:
        ourGoal = "G42"

    return ourGoal
