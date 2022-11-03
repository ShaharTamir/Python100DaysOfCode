from turtle import Turtle
from random import choice, randint


class Car(Turtle):
    COLORS = ["yellow", "green", "blue", "red", "orange", "purple"]

    def __init__(self, x_lim, y_lim):
        super().__init__("square", visible=False)
        self.penup()
        self.goto(x_lim, randint(-y_lim, y_lim))
        self.showturtle()
        self.color(choice(self.COLORS))
        self.setheading(180)  # move from east to west
        self.shapesize(stretch_len=2)

    def move(self):
        self.forward(10)

    def is_hit(self, item_position):
        return item_position[0] + 20 < self.xcor() and \
            self.distance(item_position) < 40
