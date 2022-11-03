import turtle as tt

tim = tt.Turtle()
screen = tt.Screen()


def move_forward():
    tim.forward(5)


def move_backward():
    tim.backward(5)


def turn_left():
    tim.left(2)


def turn_right():
    tim.right(2)


def clear_screen():
    screen.reset()
    tim.penup()
    tim.home()
    tim.pendown()


def main():
    screen.onkeypress(move_forward, "w")
    screen.onkeypress(move_backward, "s")
    screen.onkeypress(turn_left, "a")
    screen.onkeypress(turn_right, "d")
    screen.onkeypress(clear_screen, "c")
    screen.listen()

    screen.exitonclick()


if "__main__" == __name__:
    main()
