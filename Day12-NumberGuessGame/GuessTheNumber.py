from random import randint
from os import system
from GuessTheNumberArt import LOGO

LOW_RANGE = 1
HIGH_RANGE = 100
EASY_LVL = 10
HARD_LVL = 5


def make_guess():
    return int(input("Make a guess: "))


def evaluate(number, guess):
    if number == guess:
        print(f"You got it! the answer was {number}")
        return True
    elif number < guess:
        print("Too high.")
    elif number > guess:
        print("Too low.")
    return False


def guess_the_num_game():
    system("clear")
    print(LOGO)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    number = randint(LOW_RANGE, HIGH_RANGE)
    attempts = HARD_LVL
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

    if "easy" == difficulty:
        attempts = EASY_LVL

    while attempts:
        print(f"You have {attempts} attempts remaining to guess the number.")
        if evaluate(number, make_guess()):
            return    # win the game. finish
        else:
            attempts -= 1

    print("You've run out of guesses, you lose.")


if __name__ == "__main__":
    guess_the_num_game()
