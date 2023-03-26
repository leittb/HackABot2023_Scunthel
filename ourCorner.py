def isInFront(botCoords,BallCoords):
    angle = math.atan2(botCoords[1]-BallCoords[1],botCoords[0]-BallCoords[0])
    angle_diff = botCoords[2] - angle
    angleTol = 0.15
    if abs(angle_diff)<angleTol and euclidean_distance(botCoords,BallCoords)<130:
        return True
    return False

def isInOurCorner():
    bullCoords = locations["M7"]
    grabberCoords = locations["M8"]
    ballCoords =  locations["B"]

    #bull dozer keeps
    bullDistToGoal = euclidean_distance([bullCoords[0], bullCoords[1]], [ourGoal[0],ourGoal[1]])
    if bullDistToGoal > 50:
        move_towards(7, [bullCoords[0], bullCoords[1]], [ourGoal[0],ourGoal[1]])
    else:
        move_bot(7,0,0)

    #needs to know to rotate
    if( isInFront(grabberCoords,grabberCoords)):
        move_towards(8, [grabberCoords[0], grabberCoords[1]], [oppGoal[0],oppGoal[1]])
    else:
        #grapper collects
        move_towards(8, [grabberCoords[0], grabberCoords[1]], [ballCoords[0],ballCoords[1]])
