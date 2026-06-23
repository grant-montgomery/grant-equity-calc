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
    p1card1 = Card("h", 7)
    p1card2 = Card("h", 6)
    p2card1 = Card("s", 6)
    p2card2 = Card("s", 7)
    player1.predetermined_hand(p1card1, p1card2, deck)
    player2.predetermined_hand(p2card1, p2card2, deck)
    # player1.print_hand()
    # player2.print_hand()
    # deck.deal_full_board(table)
    deck.deal_specific_board(table)

    # print(f'{table.board=}')
    # print(f'{table.seated_players=}')
    # print(deck)

    determine_hand_strength(table) # FLUSH CHECKER NEEDS DEBUGGING


    # Print each player's hand strength
    for dude in table.seated_players:
        print(f'{dude}\'s hand with pairs removed: {dude.hand_without_pairs}')
        print(f'{dude}\'s full hand: {dude.hand_plus_board}')
        print(f'{dude}\'s Hand Ranking: {dude.hand_class} -- Best five card hand: {dude.best_five}')


main()