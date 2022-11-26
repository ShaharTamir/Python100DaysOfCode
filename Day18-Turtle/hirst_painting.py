from turtle import Turtle, dot, Screen, penup, pendown, colormode
from random import choice
import colorgram

#app window size numXnum
WINDOW = 750
#dots config
SPACE = 50
DOT_SIZE = 20
START_X = -200
START_Y = -275
DOTS_IN_ROW = 10
NUM_DOTS_ROWS = 10
#colors extraction
WHITE = 245
COLORS_TO_EXTRACT = 30
COLOR_MODE_TUPLE = 255


def extract_colors_rgb(image_path, num_colors):
    colors_objects = colorgram.extract(image_path, num_colors)
    colors = []
    for color in colors_objects:
        if color.rgb.r < WHITE or color.rgb.g < WHITE or color.rgb.b < WHITE:
            new_color = (color.rgb.r, color.rgb.g, color.rgb.b)
            colors.append(new_color)
    return colors


def draw_line_of_dots(t, colors, num_dots):
    for _ in range(num_dots):
        rand_color = choice(colors)
        t.dot(DOT_SIZE, rand_color)
        t.forward(SPACE)


def new_line_position(t):
    t.setx(START_X)
    t.sety(round(t.ycor()) + SPACE)


def hirst_paint():
    t = Turtle()
    t.penup()
    t.hideturtle()
    t.speed("fast")
    screen = Screen()
    screen.setup(WINDOW, WINDOW)
    screen.colormode(COLOR_MODE_TUPLE)
    colors = extract_colors_rgb("Addictive---detail-of-Dam-007.webp", COLORS_TO_EXTRACT)
    t.setposition(START_X, START_Y)

    for _ in range(NUM_DOTS_ROWS):
        new_line_position(t)
        draw_line_of_dots(t, colors, DOTS_IN_ROW)
    screen.exitonclick()


if "__main__" == __name__:
    hirst_paint()



