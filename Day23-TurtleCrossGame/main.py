from turtle import Screen
from time import sleep
from level import Level
from player import Player
from car import Car

HEIGHT = 600
WIDTH = 800
OFFSET = 20

game_run = True
screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.tracer(0)
lvl = Level((-WIDTH / 2 - OFFSET, HEIGHT / 2 - OFFSET))
player = Player(HEIGHT / 2 - OFFSET)
cars = []
car = Car(WIDTH / 2 + OFFSET, HEIGHT / 2 - 2 * OFFSET)
cars.append(car)

screen.onkeypress(fun=player.move, key="Up")
screen.listen()
car_gen_count = 0

while game_run:
    lvl.draw()
    screen.update()
    sleep(lvl.speed)
    if car_gen_count >= lvl.gen_car_speed:
        cars.append(Car(WIDTH / 2 + OFFSET, HEIGHT / 2 - 2 * OFFSET))
        car_gen_count = 0
    else:
        car_gen_count += 1

    for car in cars:
        car.move()
        if car.is_hit(player.position()):
            game_run = False

    if player.is_crossed():
        player.return_to_start()
        lvl.next_level()

lvl.game_over()
screen.update()
screen.exitonclick()
