from turtle import Turtle


class ScoreBoard(Turtle):
    ALIGN = "center"
    FONT = "Courier"
    SIZE = 18
    FONT_STYLE = "italic bold"
    FONT_FORMAT = (FONT, SIZE, FONT_STYLE)

    def __init__(self, height):
        super().__init__(visible=False)
        self.score = 0
        self.penup()
        self.goto(0, height)
        self.color("grey")

    def present_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align=self.ALIGN,
                   font=self.FONT_FORMAT)

    def add_score(self):
        self.score += 1

    def game_over(self):
        self.home()
        self.write("GAME OVER", align=self.ALIGN, font=self.FONT_FORMAT)
