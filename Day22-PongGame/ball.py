from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__(shape="circle")
        self.shapesize(0.6)
        self.penup()
        self.color("white")
        self.x_move = 10
        self.y_move = 10
        self.game_speed = 0.05

    def reset_ball(self, direction=None):
        self.home()
        self.game_speed = 0.05
        self.bounce_x()

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.game_speed *= 0.9
