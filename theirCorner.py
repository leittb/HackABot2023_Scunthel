def isInTheirCorner():
    bullCoords = locations["M7"]
    grabberCoords = locations["M8"]
    ballCoords =  locations["B"]

    #bull mid blocks
    newXY = [(ballCoords[0] + ourGoal[0])/2, (ballCoords[1] + ourGoal[1])/2]
    move_towards(8, [bullCoords[0], bullCoords[1]], [newXY[0],newXY[1]])

    #grabber keeps
    grabberDistToGoal = euclidean_distance([grabberCoords[0], grabberCoords[1]], [ourGoal[0],ourGoal[1]])
    if grabberDistToGoal > 50:
        move_towards(8, [grabberCoords[0], grabberCoords[1]], [ourGoal[0],ourGoal[1]])
    else:
        move_bot(8,0,0)
