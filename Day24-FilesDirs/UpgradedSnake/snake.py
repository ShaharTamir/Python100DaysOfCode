from turtle import Turtle


class Snake:
    STEP = 10
    SENSITIVITY = 9
    TURN_ANGLE = 90.0
    INIT_POS = [(0, 0), (-10, 0), (-20, 0)]
    DIR = {"east": 0, "north": 90, "west": 180, "south": 270}

    def __init__(self):
        self.body = []
        self.head = None
        self.create_snake()

    def create_snake(self):
        for pos in self.INIT_POS:
            self.add_body_part(pos)
        self.head = self.body[0]

    def add_body_part(self, pos=None):
        new_body_part = Turtle("square")
        new_body_part.shapesize(0.5, 0.5)
        new_body_part.color("white")
        new_body_part.penup()
        if pos is not None:
            new_body_part.goto(pos)
        self.body.append(new_body_part)

    def move(self):
        for body_part in range(len(self.body) - 1, 0, -1):
            self.body[body_part].goto(self.body[body_part - 1].position())

        self.head.forward(self.STEP)

    def is_food_eaten(self, apple):
        return self.head.distance(apple) < self.SENSITIVITY

    def is_hit_wall(self, x_lim, y_lim):
        return self.head.xcor() >= x_lim / 2 or \
            self.head.xcor() <= -x_lim / 2 or \
            self.head.ycor() >= y_lim / 2 or \
            self.head.ycor() <= -y_lim / 2

    def is_hit_itself(self):
        for part in self.body[1:]:
            if self.head.position() == part.position():
                return True
        return False

    def reset(self):
        for part in self.body:
            part.reset()
        self.body.clear()
        self.create_snake()

    def turn_left(self):
        self.__turn("east", "west")

    def turn_right(self):
        self.__turn("west", "east")

    def turn_up(self):
        self.__turn("south", "north")

    def turn_down(self):
        self.__turn("north", "south")

    def __turn(self, limit, turn_to):
        if self.head.heading() != self.DIR[limit]:
                self.head.setheading(self.DIR[turn_to])

