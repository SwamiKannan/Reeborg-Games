def turn_right():
    for _ in range(3):
        turn_left()
    
def ascend():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    while wall_on_right():
        move()
        
def descend():
    turn_right()
    while front_is_clear():
        move()
    turn_left()
        
while not at_goal():
    if front_is_clear():
        move()
    elif wall_in_front():
        ascend()
        descend()
        

    