from turtle import Turtle, Screen
from time import sleep
from snake import Snake
from food import Food
from score_board import ScoreBoard

WIDTH = 600
HEIGHT = 600
APPLE_WIDTH_LIM = WIDTH / 2 - 100
APPLE_HEIGHT_LIM = HEIGHT / 2 - 100
game_running = True
screen = Screen()
screen.title("Snake Game")
screen.setup(WIDTH, HEIGHT)
screen.bgcolor("black")
screen.tracer(0)


def finish_game():
    global game_running
    game_running = False


snake = Snake()
apple = Food(APPLE_WIDTH_LIM, APPLE_HEIGHT_LIM)
score = ScoreBoard(APPLE_HEIGHT_LIM)

screen.onkeypress(fun=snake.turn_right, key="Right")
screen.onkeypress(fun=snake.turn_left, key="Left")
screen.onkeypress(fun=snake.turn_up, key="Up")
screen.onkeypress(fun=snake.turn_down, key="Down")
screen.onkeypress(fun=finish_game, key="space")
screen.listen()

while game_running:
    screen.update()
    sleep(0.05)
    if snake.is_food_eaten(apple.position()):
        score.add_score()
        snake.add_body_part()
        apple.gen_apple()
    snake.move()
    score.present_score()
    if snake.is_hit_wall(WIDTH, HEIGHT) or snake.is_hit_itself():
        game_running = False

score.game_over()
screen.exitonclick()
