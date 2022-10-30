from turtle import *
from random import choice, randint

CIRCLE = 360
ANGLE_INC = 5
STEP_LEN = 20


def dashed_line(turt, length):
    flag = 0
    for i in range(length):
        if 0 == i % 4:
            flag = not flag
            if flag:
                turt.penup()
            else:
                turt.pendown()
        turt.forward(1)


def draw_shape(turt, side_len, num_sides):
    angle = CIRCLE // num_sides
    for _ in range(num_sides):
        turt.forward(side_len)
        turt.right(angle)


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)

    return (r, g, b)


def random_walk(turt, steps):
    turt.speed("fast")
    angles = [0, 90, 180, 270]
    turt.pensize(10)
    for _ in range(steps):
        angle = choice(angles)
        turt.pencolor(random_color())
        turt.forward(STEP_LEN)
        turt.setheading(angle)
    turt.speed("normal")


def draw_spirograph(turt, radius):
    tim.speed("fastest")
    for _ in range(1, CIRCLE, ANGLE_INC):
        turt.pencolor(random_color())
        turt.circle(radius)
        turt.left(ANGLE_INC)
    tim.speed("normal")


tim = Turtle()
screen = Screen()
screen.colormode(255)
# dashed_line(tim, 100)
# for i in range(3, 10):
#     draw_shape(tim, 50, i)
# random_walk(tim, 100)
draw_spirograph(tim, 100)
screen.exitonclick()
