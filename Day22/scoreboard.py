from turtle import Turtle


class Score(Turtle):
    STYLE = ("ariel", 18, "bold")

    def __init__(self, position=(0, 0)):
        super().__init__(visible=False)
        self.penup()
        self.color("white")
        self.goto(position)
        self.__score = 0

    def add_score(self):
        self.__score += 1

    def draw_score(self):
        self.clear()
        self.write(f"{self.__score}", align="center", font=self.STYLE)
