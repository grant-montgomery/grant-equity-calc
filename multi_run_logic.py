from kickers import find_biggest_pair
from player import *
from showdown import determine_hand_strength
import random

def get_players(deck, table):
    """
    Creates x Player objects subject to user input
    :param deck: deck object containing cards
    :param table: table object for containing list of seated players
    :return: none
    """
    number_of_players = int(input("Enter number of players (2-6): "))
    for num in range(number_of_players):
        Player(deck, table)


def get_number_of_players():
    number_of_players = int(input("Enter number of players (2-6): "))
    return number_of_players

def get_hands(deck, table):
    """
    function for getting user input for hands for all players
    :param deck: deck object containing cards
    :param table: table object containing list of seated players
    :return:
    """

    for player in table.seated_players:
        hand = input(f"Please enter the hand for {player}")

        rank1 = int(hand[0])
        suit1 = hand[1]
        rank2 = int(hand[2])
        suit2 = hand[3]
        card1 = deck.draw_specific(rank1, suit1)
        card2 = deck.draw_specific(rank2, suit2)
        player.hand.append(card1)
        player.hand.append(card2)


def get_hands_parsed(deck, table):
    """
    function for getting user input for hands for all players
    :param deck: deck object containing cards
    :param table: table object containing list of seated players
    :return:
    """
    for player in table.seated_players:
        print(f"Time to enter {player}'s cards")
        rank_1 = int(input("Card 1 rank: "))
        suit_1 = input("Card 1 suit: ")
        rank_2 = int(input("Card 2 rank: "))
        suit_2 = input("Card 2 suit: ")
        card_1 = deck.draw_specific(rank_1, suit_1)
        card_2 = deck.draw_specific(rank_2, suit_2)
        player.hand.append(card_1)
        player.hand.append(card_2)



def determine_winner(table, player1, player2):
    """
    function for figuring out who won the hand.
    :param player2: player object containing hand
    :param player1: player object containing hand
    :param table: table object containing list of players
    :return: int, corresponds to winning player's player number
    """


    player_hand_classes = []
    winners_index = []
    for player in table.seated_players:
        player_hand_classes.append(player.hand_class)

    high_hand = max(player_hand_classes)
    for h_class in player_hand_classes:
        if h_class == high_hand:
            winners_index.append(player_hand_classes.index(h_class))
    for player in table.seated_players:
        if player.hand_class == high_hand:
            table.tied_players.append(player)

        # CHANGE LATER: FOLLOWING LINE EXCLUDES TIES ALTOGETHER
        # you can just get rid of the else and untab the next block to go back to including ties
    if len(winners_index) > 1 and high_hand == 1:
        find_biggest_pair(table, player1, player2)
    elif len(winners_index) > 1:
        print(f"MULTIPLE WINNERS DETECTED: {len(winners_index)=}")
        table.skipped_runs += 1

    else:
        for player in table.seated_players:
            for winner in winners_index:
                if table.seated_players.index(player) == winner:
                    print(f"WINNER: {player} wins the hand with {player.best_five} -- Hand Class = {player.hand_class}")
                    player.wins += 1



def clear_player_attributes(table):
    # clear attributes of all players except their hand. to be used after a run.
    for player in table.seated_players:
        player.ranks_dict = {key: 0 for key in range(2, 15)}
        player.suits_dict = {key: 0 for key in SUITS}
        player.best_five = []
        player.hand_plus_board = []
        player.hand_class = 0
        player.kickers = []
        player.quads = []
        player.ranks_list = []
        player.straight_flush = []
        player.straight = []
        player.flush_cards_list = []
        player.full_house = []
        player.hand_without_pairs = []
        player.pairs = []
        player.trips = []
        player.two_pair = []


def run_monte_carlo_sim(number_of_runs, deck, table, player1, player2):
    """
    function for performing the monte carlo sims in order to
    determine equity
    :param number_of_runs: how many runouts to simulate (higher number
    leads to a more accurate equity estimation)
    :param deck: object containing the list of deck cards
    :param table: table object containing list of players
    :return: none, changes player.equity to reflect each player's equity
    """

    for _ in range(number_of_runs):
        # deal the board
        deck.deal_full_board(table)


        # determine hand class of each player
        determine_hand_strength(table)

        # Print each player's hand strength
        # for player in table.seated_players:
        #     print(f'{player}\'s hand with pairs removed: {player.hand_without_pairs}')
        #     print(f'{player}\'s full hand: {player.hand_plus_board}')
        #     print(f'{player}\'s Hand Ranking: {player.hand_class} -- Best five card hand: {player.best_five}')

        # determine the winner and add +1 to their wins count and print the winners hand/class
        for player in table.seated_players:
            print(f"{player.best_five=} {player.hand_class=}")
        determine_winner(table, player1, player2)

        # put the cards from the board back into the deck
        for card in table.board:
            deck.cards.append(card)
        random.shuffle(deck.cards)

        # clear all attributes of player except wins and hand
        clear_player_attributes(table)
        table.board = []
        table.tied_players = []
        # print line to separate outputs
        print("------------------------------NEW HAND---------------------------------")

    # determine equity of each player
    for player in table.seated_players:
        equity = 0
        equity = player.wins / (number_of_runs - table.skipped_runs)
        player.equity = round(equity*100, 4)
        print(f"{player} Equity: {player.equity} with {player.hand}")