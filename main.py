import random
from deck import Deck, Card, Table
from player import Player
# new program for equity calculation on two hold em hands

# hand ranking system; reflected in Player.hand_class:
# 0 - high card
# 1 - one pair
# 2 - two pair
# 3 - three of a kind
# 4 - straight
# 5 - flush
# 6 - full house
# 7 - quads
# 8 - straight flush
# 9 - royal flush

def main():
    deck = Deck()
    table = Table()
    random.shuffle(deck.cards)
    player_1 = Player(deck, table)
    player_2 = Player(deck, table)
    player_1.print_hand()
    player_2.print_hand()
    deck.deal_full_board(table)

    print(f'{table.board=}')
    print(f'{table.seated_players=}')
    print(deck)

main()