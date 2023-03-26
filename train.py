#checks bull is front of ball
def isBullInFront(ballCoords,bullCoords):
    angle = math.atan((bullCoords[1]-ballCoords[1])/(bullCoords[0]-ballCoords[0]))
    angle_diff = Math.pi - abs(ballCoords[2] - angle)
    angleTol = 0.1
    if abs(angle_diff)<angleTol and euclidean_distance(ballCoords,bullCoords)<120:
        return True
    return False

def move_towards(mona_id, mona_loc, target_loc):
    angle = math.atan((target_loc[1]-mona_loc[1])/(target_loc[0]-mona_loc[0]))
    angle_diff = mona_loc[2] - angle
    tol = 0.1
    if (angle_diff > tol):
        move_bot(mona_id,60-(60*abs(angle_diff)/math.pi),60)
    elif (angle_diff < -tol):
        move_bot(mona_id,60,60-(60*abs(angle_diff)/math.pi))
    else:
        move_bot(mona_id,120,120)

def trainToGoal():
    bullCoords = locations["M7"]
    grabberCoords = locations["M8"]
    c0Coords = locations["C0"]
    #train to goal
    #bull peels away
    bullDistanceToGoal = euclidean_distance(oppGoal[0],oppGoal[1], bullCoords[0],bullCoords[1])
    if bullDistanceToGoal < 200:
        move_towards(7,[bullCoords[0],bullCoords[1]] , [bullCoords[0],c0Coords[1]] )
    else:
        move_towards(7,[bullCoords[0],bullCoords[1]] , [oppGoal[0],oppGoal[1]] )

    move_towards(8,[grabberCoords[0],grabberCoords[1]] , [oppGoal[0],oppGoal[1]] )


#+=200 length
def moveBullToFront(bullCoords, grabberCoords):
    if(not(isBullInFront() ) :
        #work out which x + y go
        newX = -math.sin(grabberCoords[2])*200
        newY = math.cos(grabberCoords[2])*200

        #move bots there
        move_towards(7,[bullCoords[0], bullCoords[1]] , [newX,newY])

    else:
        #start train
        trainToGoal()
