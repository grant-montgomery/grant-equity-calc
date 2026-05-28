import random
from deck import Deck, Card, Table
from player import Player
from showdown import *
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
    # random.shuffle(deck.cards)
    player1 = Player(deck, table)
    player2 = Player(deck, table)
    p1card1 = Card("c", 5)
    p1card2 = Card("h", 5)
    p2card1 = Card("c", 9)
    p2card2 = Card("c", 8)
    player1.predetermined_hand(p1card1, p1card2, deck)
    player2.predetermined_hand(p2card1, p2card2, deck)
    player1.print_hand()
    player2.print_hand()
    deck.deal_full_board(table)

    print(f'{table.board=}')
    print(f'{table.seated_players=}')
    print(deck)

    showdown(player1, player2, table)
    straight_checker(player2, table)

main()