# Function to check who has possession. Any iterals in the conditional statements will need to be tweaked for better constraints
# Returns 0 if other team has possession
# Returns 1 if we have possession
# Returns 2 if no one has possession

for (bot, metric) in locations.items():
    ball_x = locations['B'][0]
    ball_y = locations['B'][1]
    dude_x = locations[bot][0]
    dude_y = locations[bot][1]
    if bot == 'M7':
        if ball_x < dude_x and ball_x > dude_x - 180 and ball_y < dude_y + 100 and ball_y > dude_y - 60:
            return 1
    else:
        if ball_x < dude_x + 80 and ball_x > dude_x - 180 and ball_y < dude_y + 100 and ball_y > dude_y - 60:
            return 0
return 2