from turtle import Turtle


class Player(Turtle):
    STEP = 20

    def __init__(self, position=None):
        super().__init__("square")
        self.shapesize(stretch_wid=0.3, stretch_len=4)
        self.setheading(90)
        self.penup()
        self.color("white")
        if position is not None:
            self.goto(position)

    def move_up(self):
        self.forward(self.STEP)

    def move_down(self):
        self.backward(self.STEP)
