# run this at https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

def turn_right():
    for i in range(3):
        turn_left()


while not at_goal():
    if not wall_in_front():
        move()
    if False == wall_on_right():
        turn_right()
    else:
        turn_left()
