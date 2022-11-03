import turtle as tt
from random import choice

LOWEST_TURTLE_HEIGHT = -100
START_LINE = -300
WIDTH = 700
HEIGHT = 500
TURTLES_DIST = 50
STEP = 5
FINISH_LINE = WIDTH / 2 - 25


def create_racers():
    turtles_family = []
    colors = ["yellow", "red", "purple", "blue", "green"]

    for color in colors:
        new_turt = tt.Turtle()
        new_turt.shape("turtle")
        new_turt.color(color)
        new_turt.penup()
        turtles_family.append(new_turt)

    return turtles_family


def setup_starting_points(t_fam):
    start_height = LOWEST_TURTLE_HEIGHT
    for t in t_fam:
        t.setposition(x=START_LINE, y=start_height)
        start_height += TURTLES_DIST


def start_race(t_fam):
    while True:
        t = choice(t_fam)
        t.forward(STEP)
        if t.xcor() >= FINISH_LINE:
            return t.pencolor()


def run_turtle_racing():
    screen = tt.Screen()
    screen.setup(WIDTH, HEIGHT)
    user_bet = screen.textinput("winning turtle color", "Who will win the race? enter a color:")
    if user_bet is not None:
        turtles = create_racers()
        setup_starting_points(turtles)
        winner = start_race(turtles)
        if winner == user_bet:
            print("Your turtle won!")
        else:
            print(f"Sorry, you lose.. winner is {winner}")


if "__main__" == __name__:
    run_turtle_racing()
