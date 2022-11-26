from turtle import Turtle
from random import randint


class Food(Turtle):

    def __init__(self, width_limit, height_limit):
        self.x_limit = width_limit
        self.y_limit = height_limit
        super().__init__(shape="circle", visible=False)
        self.color("red")
        self.penup()
        self.gen_apple()

    def gen_apple(self):
        x_coordinate = float(randint(-self.x_limit, self.x_limit))
        y_coordinate = float(randint(-self.y_limit, self.y_limit))
        self.hideturtle()
        self.setposition(x_coordinate, y_coordinate)
        self.shapesize(0.3)
        self.showturtle()
