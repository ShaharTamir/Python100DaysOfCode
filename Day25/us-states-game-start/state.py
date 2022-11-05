from turtle import Turtle


class State(Turtle):
    STYLE = ("Courier", 10, "normal")

    def __init__(self, xcor, ycor, name):
        super().__init__(visible=False)
        self.penup()
        self.goto(int(xcor), int(ycor))
        self.write(name)
