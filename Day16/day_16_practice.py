# from turtle import Turtle, Screen
#
# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("coral")
# timmy.speed("slowest")
# timmy.forward(50)
# timmy.left(90)
# timmy.forward(50)
# timmy.left(90)
# timmy.forward(50)
# timmy.left(90)
# timmy.forward(50)
#
# my_screen = Screen()
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
print(table)
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
print(table)