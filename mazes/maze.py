def turn_around():
    for _ in range(2):
        turn_left()
        
def turn_right():
    turn_around()
    turn_left()

def change_north_position():
    while not is_facing_north():
        turn_left()

change_north_position()

while front_is_clear():
    move()
def check_step():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
        
while not at_goal():
    check_step()
        