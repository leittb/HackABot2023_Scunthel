# Function to check who has possession. Any iterals in the conditional statements will need to be tweaked for better constraints
# Returns 0 if other team has possession
# Returns 1 if we have possession
# Returns 2 if no one has possession

def who_has_possession(dict):
    for (bot, metric) in dict.items():
        ball_x = dict['B'][0]
        ball_y = dict['B'][1]
        dude_x = dict[bot][0]
        dude_y = dict[bot][1]
        if bot == 'M7':
            if ball_x < dude_x and ball_x > dude_x - 200 and ball_y < dude_y + 100 and ball_y > dude_y - 40:
                return 1
        else:
            if ball_x < dude_x + 90 and ball_x > dude_x - 200 and ball_y < dude_y + 100 and ball_y > dude_y - 40:
                return 0
    return 2