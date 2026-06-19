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
    p1card1 = Card("s", 14)
    p1card2 = Card("h", 5)
    p2card1 = Card("h", 8)
    p2card2 = Card("s", 9)
    player1.predetermined_hand(p1card1, p1card2, deck)
    player2.predetermined_hand(p2card1, p2card2, deck)
    player1.print_hand()
    player2.print_hand()
    # deck.deal_full_board(table)
    deck.deal_specific_board(table)

    print(f'{table.board=}')
    print(f'{table.seated_players=}')
    print(deck)

    determine_hand_strength(table)
    # remove_pairs(player1)
    # remove_pairs(player2)
    # straight_checker(player2, table)
    # straight_checker(player1, table)
    # print(f"{player1.pairs=}")
    # print(f"{player1.hand_without_pairs=}")
    # print(f"{player2.hand_without_pairs=}")
    # fill_ranks_dict(player1)
    # fill_ranks_dict(player2)
    # fill_suits_and_ranks_dicts(table)
    # print(f"{player1.ranks_dict=}")
    # print(f"{player1.suits_dict=}")
    # print(f"{player2.ranks_dict=}")
    # print(f"{player2.suits_dict=}")

    # Print each player's hand strength
    for dude in table.seated_players:
        print(f'{dude}\'s Hand Ranking: {dude.hand_class} -- Best five card hand: {dude.best_five}')
        print(f"{dude.full_house=}")

main()