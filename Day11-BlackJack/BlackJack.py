from random import randint
from os import system
from BlackJackArt import logo

blackjack = 21
computer_limit = 17
ase = 11


def is_game_on():
    return 'y' == \
      input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")


def pick_a_card(card_pack):
    index_to_card_offset = 2
    while True:
        card = randint(0, len(card_pack) - 1)
        if 0 != card_pack[card]:
            card_pack[card] -= 1
            return card + index_to_card_offset


def add_card_to_hand(hand, cards_pack):
    hand.append(pick_a_card(cards_pack))
    while sum(hand) > blackjack:
        if ase in hand:
            hand[hand.index(ase)] = 1
        else:
            return True
    return False


def should_player_draw():
    return 'y' == input("Type 'y' to get another card, type 'n' to pass: ")


def print_status(player_hand, computer_hand):
    player_sum = sum(player_hand)
    print(f"  Your cards: {player_hand}, current score: {player_sum}")
    print(f"  Computer's first card: {computer_hand[0]}")


def player_part(player_hand, computer_hand, cards_pack):
    while True:
        print_status(player_hand, computer_hand)
        if should_player_draw():
            overflow = add_card_to_hand(player_hand, cards_pack)
            if overflow:
                return
        else:
            return


def computer_part(computer_hand, cards_pack):
    while True:
        overflow = add_card_to_hand(computer_hand, cards_pack)
        if overflow or sum(computer_hand) > computer_limit:
            return


def print_results(player_hand, computer_hand):
    player_sum = sum(player_hand)
    computer_sum = sum(computer_hand)
    print(f"  Your final hand: {player_hand}, final score: {player_sum}")
    print(f"  Computer's final hand: {computer_hand}, final score: {computer_sum}")

    if player_sum > blackjack and computer_sum > blackjack:
        print("You went over. You lose 😤")
    elif player_sum > blackjack:
        print("You went over. You lose 😭")
    elif computer_sum > blackjack:
        print("Opponent went over. You win 😁")
    elif player_sum == computer_sum:
        print("Draw 🙃")
    elif player_sum == blackjack:
        print("Win with a Blackjack 😎")
    elif computer_sum == blackjack:
        print("Lose, opponent has Blackjack 😱")
    elif player_sum > computer_sum:
        print("You win 😃")
    else:
        print("You lose 😤")


def black_jack_game():
    if not is_game_on():
        return

    system("clear")
    print(logo)
    cards_pack = [4, 4, 4, 4, 4, 4, 4, 4, 12, 4]
    player_hand = []
    computer_hand = []

    # init game
    for i in range(0, 2):
        player_hand.append(pick_a_card(cards_pack))
        computer_hand.append(pick_a_card(cards_pack))

    # game start
    if sum(player_hand) != blackjack and sum(computer_hand) != blackjack:
        player_part(player_hand, computer_hand, cards_pack)
    else:
        print_status(player_hand, computer_hand)
    computer_part(computer_hand, cards_pack)

    # game finish
    print_results(player_hand, computer_hand)
    black_jack_game()


if __name__ == "__main__":
    black_jack_game()

