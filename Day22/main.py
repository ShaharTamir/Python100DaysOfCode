from turtle import Screen
from time import sleep
from scoreboard import Score
from net import Net
from ball import Ball
from player import Player

WIDTH = 800
HEIGHT = 600
TOP = HEIGHT / 2
BOTTOM = -TOP
EAST_WALL = WIDTH / 2
WEST_WALL = -EAST_WALL
SCORE_POS = [(150, 250), (-150, 250)]
PLAYER_START_POS = [(350, 0), (-350, 0)]
WALLS = [EAST_WALL, WEST_WALL]
BOUNCE_SENSITIVITY = 20
BALL_DIST = 50

game_on = True
screen = Screen()
screen.bgcolor("black")
screen.setup(WIDTH, HEIGHT)
screen.tracer(0)

players = []
for pos in range(len(SCORE_POS)):
    new_player = {
        "player": Player(PLAYER_START_POS[pos]),
        "score": Score(SCORE_POS[pos]),
        "wall": WALLS[pos]
    }
    new_player["score"].draw_score()
    players.append(new_player)

net = Net(lowest_y=BOTTOM, highest_y=TOP)
ball = Ball()
screen.update()

# setup keys
screen.onkeypress(fun=players[0]["player"].move_up, key="Up")
screen.onkeypress(fun=players[0]["player"].move_down, key="Down")
screen.onkeypress(fun=players[1]["player"].move_up, key="w")
screen.onkeypress(fun=players[1]["player"].move_down, key="s")
screen.listen()

while game_on:
    sleep(ball.game_speed)
    ball.move()

    ball_x = ball.xcor()
    ball_y = ball.ycor()
    # check collision with top or bottom
    if ball_y > TOP - BOUNCE_SENSITIVITY or \
       abs(ball_y) > abs(BOTTOM) - BOUNCE_SENSITIVITY:
        ball.bounce_y()

    for i in range(len(players)):
        # check for collision with players paddle
        if abs(ball_x) > abs(PLAYER_START_POS[i][0]) - BOUNCE_SENSITIVITY and \
           ball.distance(players[i]["player"]) < BALL_DIST:
            ball.bounce_x()
        # check for point
        elif abs(ball_x) >= abs(players[i]["wall"]):
            players[i]["score"].add_score()
            ball.reset_ball()
        players[i]["score"].draw_score()
    screen.update()

screen.exitonclick()
