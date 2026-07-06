import random
from deck import *
from player import Player
from showdown import *
from multi_run_logic import *
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

    # Get user inputs
    # get_players(deck, table)
    # get_hands_parsed(deck, table)

    # TESTING HANDS
    player1 = Player(deck, table)
    player2 = Player(deck, table)



    card1 = deck.draw_specific(13, "h")
    card2 = deck.draw_specific(14, "h")
    card3 = deck.draw_specific(2, "s")
    card4 = deck.draw_specific(2, "c")
    player1.hand.append(card1)
    player1.hand.append(card2)
    player2.hand.append(card3)
    player2.hand.append(card4)


    # # deal the board
    # deck.deal_full_board(table)
    #
    # # determine hand class of each player
    # determine_hand_strength(table)


    run_monte_carlo_sim(1000, deck, table, player1, player2)

    # determine_winner(table)


    # debugging outputs
    print((table.skipped_runs/1000) * 100) # for 1000 runs prints percent of skipped ties

main()



