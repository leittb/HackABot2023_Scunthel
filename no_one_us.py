import math

def euclidean_distance(l1, l2):
    return math.sqrt((l2[0] - l1[0])**2 + (l2[1] - l1[1])**2)

def bearing(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    delta_x = x2 - x1
    delta_y = y2 - y1
    radians = math.atan2(delta_y, delta_x)
    degrees = math.degrees(radians)
    return (degrees + 360) % 360

def block_movement(dict,block_id, goal_coord):
    block_coord = dict[block_id]
    ball_coord = dict["B"]

    # Calculate the slope and y-intercept of the line between point1 and point2
    slope = (goal_coord[1] - ball_coord[1]) / (goal_coord[0] - ball_coord[0])
    y_intercept = ball_coord[1] - slope * ball_coord[0]

    # Find the nearest point on the line to point3
    x_nearest = (block_coord[0] + slope * block_coord[1] - slope * y_intercept) / (1 + slope**2)
    y_nearest = slope * x_nearest + y_intercept
    point_nearest = (x_nearest, y_nearest)
    return point_nearest

def defense_is_cool():
    dozer = locations['M7']
    grabber = locations['M8']

    move_towards(7, [dozer[0], dozer[1]], block_movement(locations, robot_to_intercept, ourGoal))

    grabberDistToGoal = euclidean_distance([grabber[0], grabber[1]], [ourGoal[0],ourGoal[1]])
    if grabberDistToGoal > 50:
        move_towards(8, [grabber[0], grabber[1]], [ourGoal[0],ourGoal[1]])
    else:
        move_bot(8,0,0)

    