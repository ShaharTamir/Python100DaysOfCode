from turtle import Turtle


class ScoreBoard(Turtle):
    ALIGN = "center"
    FONT = "Courier"
    SIZE = 18
    FONT_STYLE = "italic bold"
    FONT_FORMAT = (FONT, SIZE, FONT_STYLE)
    FILE_NAME = "highscore.txt"

    def __init__(self, height):
        super().__init__(visible=False)
        self.score = 0
        self.high_score = 0
        try:
            score_file = open(self.FILE_NAME, "r")
            self.high_score = int(score_file.read())
        except:
            pass
        self.penup()
        self.goto(0, height)
        self.color("grey")

    def update_score_board(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", align=self.ALIGN,
                   font=self.FONT_FORMAT)

    def add_score(self):
        self.score += 1
        if self.score > self.high_score:
            self.high_score = self.score

    def reset(self):
        with open(self.FILE_NAME, "w+") as highscore_mem:
            highscore_mem.write(str(self.high_score))
        self.score = 0
