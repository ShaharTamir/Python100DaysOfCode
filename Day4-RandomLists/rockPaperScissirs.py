'''
Make a rock, paper, scissors game.

Start the game by asking the player:

"What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."

From there you will need to figure out:

- How you will store the user's input.
- How you will generate a random choice for the computer.
- How you will compare the user's and the computer's choice to determine the winner (or a draw).
- And also how you will give feedback to the player.

'''
from random import randint
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

options = [rock, paper,scissors]
tie = "it's a tie!"
you_win = "congrats! you win!"
you_lose = "oh snap.. you lose!"
game_options = [[tie, you_lose, you_win],
                [you_win, tie, you_lose],
                [you_lose, you_win, tie]]

user_move = int(input("What do you choose? Type 0 for Rock,\
 1 for Paper or 2 for Scissors. "))
computer_move = randint(0, 2)

print(options[user_move])
print("\ncomputer chose: \n")
print(options[computer_move])

print(game_options[user_move][computer_move])