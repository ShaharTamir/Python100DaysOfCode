import random
from os import system

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

end_of_game = False
with open('/usr/share/dict/american-english', 'r') as file:
  word_list = file.read().split('\n')
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

answer = []
for i in chosen_word:
  answer.append('_')

lives = len(stages)

while False == end_of_game:
  count = 0
  for i in answer:
    print(i + ' ', end='')
  guess = input('\nGuess a letter: ').lower()
  system('clear')

  if guess in answer:
    print("you have already found that letter")
    continue

  for i, val in enumerate(chosen_word):
    if guess == val:
      answer[i] = guess
      count += 1

  if count == 0:
    print(f'{guess} is not in the word')
    lives -= 1

  if '_' in answer == False:
    end_of_game = True
    print('YOU WIN!')
  else:
    if 1 == lives:
      end_of_game = True
      print(f'The word was: {chosen_word}\nYOU LOSE... ')
    print(stages[lives - 1])
