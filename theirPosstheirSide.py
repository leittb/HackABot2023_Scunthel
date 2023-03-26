

def euclidean_distance(l1, l2):
    return math.sqrt((l2[0] - l1[0])**2 + (l2[1] - l1[1])**2)

def midBlock():
    #their side their possession defence
    #can wait and block
    bullCoords = locations["M7"]
    grabberCoords = locations["M8"]
    ballCoords =  locations["B"]

    #bull tackles
    move_towards(7, [bullCoords[0], bullCoords[1]], [ballCoords[0],ballCoords[1]])

    #grabber blocks halfway
    newXY = [(ballCoords[0] + ourGoal[0])/2, (ballCoords[1] + ourGoal[1])/2]
    move_towards(8, [grabberCoords[0], grabberCoords[1]], [newXY[0],newXY[1]])
