from menu import MENU
from coins import COINS

OFF = 'off'
REPORT = 'report'
AMOUNT = 0
UNITS = 1


def menu_string_format(keys):
    menu_str = ''
    for i in keys:
        menu_str += f'{i}/'
    return menu_str


def print_report(status):
    for key, val in status.items():
        if key == "money":
            print(f"{key.title()}: {val[UNITS]}{val[AMOUNT]}")
        else:
            print(f"{key.title()}: {val[AMOUNT]}{val[UNITS]}")


def verify_ingredients(status, menu_op):
    for ing_key, ing_val in menu_op["ingredients"].items():
        if status[ing_key][AMOUNT] < ing_val:
            print(f"Sorry there is not enough {ing_key}.")
            return False
    return True


def process_coins(menu_op):
    print("Please insert coins.")
    cost = float(menu_op["cost"])
    sum_coins = 0.0

    for coin, val in COINS.items():
        sum_coins += int(input(f"How many {coin}s?: ")) * val

    if sum_coins < cost:
        print("Sorry that's not enough money. Money refunded.")
        return 0.0
    elif sum_coins > cost:
        change = sum_coins - cost
        print(f"Here is ${change:.2f} in change.")
        sum_coins -= change

    return sum_coins


def make_coffee(status, menu_op):
    for ing_key, ing_val in menu_op["ingredients"].items():
        status[ing_key][AMOUNT] -= ing_val
    status["money"][AMOUNT] += menu_op["cost"]


def make_buy(status, user_input):
    # validate user input
    for menu_op in MENU.keys():
        if user_input == menu_op and verify_ingredients(status, MENU[menu_op]):
            payment = process_coins(MENU[menu_op])
            if payment > 0.0:
                make_coffee(status, MENU[menu_op])
                print(f"Here is your {menu_op} ☕. Enjoy!")


def coffee_machine():
    machine_status = {
        "water": [300, 'ml'],
        "milk": [200, 'ml'],
        "coffee": [100, 'g'],
        "money": [0.0, '$'],
    }

    while True:
        user_input = input(f"What would you like? ({menu_string_format(MENU.keys())}): ").lower()
        if OFF == user_input:
            break
        if REPORT == user_input:
            print_report(machine_status)
        else:
            make_buy(machine_status, user_input)
    print("Goodbye!")


if "__main__" == __name__:
    coffee_machine()
