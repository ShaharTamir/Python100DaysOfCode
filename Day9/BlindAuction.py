from os import system

print("Welcome to the secret auction program.")
finish = False
bidders = {}

def find_highest_bidder(bidding_records):
  max = 0
  winner = ''

  for name, bid in bidding_records.items():
    if bid > max:
      max = bid
      winner = name

  print(f"The winner is {winner} with a bid of ${max}\n\n")


while not finish:
  name = input("What is your name?: ")
  bid = int(input ("What's your bid?: $"))
  more = input("Are there any other bidders? Type 'yes' or 'no'.\n")

  bidders[name] = bid
  finish = True if (more == 'no') else False
  system("clear")

find_highest_bidder(bidders)
