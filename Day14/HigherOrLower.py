from GameData import data
from GameArt import logo, vs
from random import choice
from os import system


def print_format(item):
    return f"{item['name']}, a {item['description']}, from {item['country']}."


def gen_next_cmp(cmp_a, cmp_b):
    while cmp_a is cmp_b:
        cmp_b = choice(data)
    return cmp_b

def print_comparison(cmp_a, cmp_b):
    print(f"Compare A: {print_format(cmp_a)}")
    print(vs)
    print(f"Against B: {print_format(cmp_b)}")


def calc_user_choice(cmp_a, cmp_b):
    A = 'A'
    B = 'B'
    user_choice = ""
    while user_choice != A and user_choice != B:
        user_choice = input(f"Who has more followers? Type {A} or {B}: ").upper()
    
    if A == user_choice:
        return cmp_a['follower_count'] >= cmp_b['follower_count']
    return cmp_b['follower_count'] >= cmp_a['follower_count']


def higher_lower_game():
    cmp_b = choice(data)
    no_lose = True
    score = -1

    while no_lose:
        score += 1
        system("clear")
        print(logo)
        cmp_a = cmp_b
        cmp_b = gen_next_cmp(cmp_a, cmp_b)
        print_comparison(cmp_a, cmp_b)
        no_lose = calc_user_choice(cmp_a, cmp_b)

    system("clear")
    print(logo)
    print(f"Sorry, that's wrong. Final score: {score}")


if "__main__" == __name__:
    higher_lower_game()

