from turtle import Turtle


class Player(Turtle):

    def __init__(self, y_lim=300):
        super().__init__("turtle")
        self.penup()
        self.y_lim = y_lim
        self.setheading(90)
        self.return_to_start()

    def return_to_start(self):
        self.goto(0, -self.y_lim)

    def move(self):
        self.forward(10)

    def is_crossed(self):
        return self.position()[1] > self.y_lim
