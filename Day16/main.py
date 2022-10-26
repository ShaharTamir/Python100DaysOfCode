from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

OFF = "off"
REPORT = "report"
menu = Menu()
cafe_maker = CoffeeMaker()
money_maker = MoneyMachine()

while True:
    user_input = input(f"What would you like? ({menu.get_items()}): ")
    if OFF == user_input:
        break
    elif REPORT == user_input:
        cafe_maker.report()
        money_maker.report()
    else:
        item = menu.find_drink(user_input)
        if item is not None and \
           cafe_maker.is_resource_sufficient(item) and \
           money_maker.make_payment(item.cost):
            cafe_maker.make_coffee(item)

print("Goodbye!")
