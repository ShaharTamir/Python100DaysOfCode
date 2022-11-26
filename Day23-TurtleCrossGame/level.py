from turtle import Turtle


class Level(Turtle):
    STYLE = ("Courier", 16, "bold")
    OFFSET = 50

    def __init__(self, top_left_corner_pos=(0, 0)):
        super().__init__(visible=False)
        self.penup()
        self.goto(top_left_corner_pos[0] + self.OFFSET,
                  top_left_corner_pos[1] - self.OFFSET)
        self.lvl = 1
        self.speed = 0.04
        self.gen_car_speed = 3

    def next_level(self):
        self.lvl += 1
        if 0 == self.lvl % 2:
            self.gen_car_speed *= 0.9
        else:
            self.speed *= 0.9

    def draw(self):
        self.clear()
        self.write(f"Level: {self.lvl}", align="left", font=self.STYLE)

    def game_over(self):
        self.home()
        self.write("GAME OVER", align="center", font=self.STYLE)