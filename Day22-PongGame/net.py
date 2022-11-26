from turtle import Turtle


class Net(Turtle):

    def __init__(self, lowest_y=0, highest_y=0):
        super().__init__(visible=False)
        self.color("white")
        self.pensize(5)
        self.setheading(90)
        self.penup()
        self.speed("fastest")
        self.bottom = lowest_y
        self.sealing = highest_y
        self.draw_dashed_line()

    def draw_dashed_line(self):
        self.goto(0, self.bottom)
        while self.ycor() < self.sealing:
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(20)
