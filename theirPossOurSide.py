def euclidean_distance(l1, l2):
    return math.sqrt((l2[0] - l1[0])**2 + (l2[1] - l1[1])**2)

def defencePressure():
    #our side their possession defence
    #need to take ball out
    bullCoords = locations["M7"]
    grabberCoords = locations["M8"]
    ballCoords =  locations["B"]

    #bull tackles
    move_towards(7, [bullCoords[0], bullCoords[1]], [ballCoords[0],ballCoords[1]])

    #move grabber to goal
    grabberDistToGoal = euclidean_distance([grabberCoords[0], grabberCoords[1]], [ourGoal[0],ourGoal[1]])
    if grabberDistToGoal > 50:
        move_towards(8, [grabberCoords[0], grabberCoords[1]], [ourGoal[0],ourGoal[1]])
    else:
        move_bot(8,0,0)
