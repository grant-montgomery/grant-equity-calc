from straights import *
from quads_trips_pairs import *
from kickers import *

def determine_hand_strength(table):
    """
    Iterate through table.seated_players and determine hand strength for each player
    :param table: object, table object containing list of players
    :return:
    """
    for person in table.seated_players:
        # prepping properties to make hand comparison easier
        combine_hand_and_board(person, table)

        fill_suits_and_ranks_dicts(person, table)
        remove_duplicate_cards(person)

        # determining if player has specific hand classes
        if person.hand_class < 8:
            quad_checker(person)
        if person.hand_class < 7:
            full_house_checker(person)
        if person.hand_class < 6:
            flush_checker(person) # TESTING THIS FUNCTION MUST STILL BE DONE
        if person.hand_class < 5:
            straight_checker(person)
        if person.hand_class < 4:
            trips_checker(person)
        if person.hand_class < 3:
            two_pair_checker(person)
        if person.hand_class < 2:
            pair_checker(person)

        find_best_kickers(person)
        person.best_five.sort(key= lambda card : card.rank)


def combine_hand_and_board(player, table):
    """
    combine players' hand and board into hand_plus_board
    :param player: player object containing hand
    :param table: table object containing board
    :return: none, adds hand and board into player.hand_plus_board
    """

    for cards in player.hand:
        player.hand_plus_board.append(cards)
    for card in table.board:
        player.hand_plus_board.append(card)
    player.hand_plus_board.sort(key= lambda card: card.rank)
    print(f"{player}'s hand combined successfully into {player.hand_plus_board}")


def remove_duplicate_cards(player):
    """
    Populate player.hand_without_pairs with all cards from hand except duplicates.
    To be used in finding straights.
    :param player: player object containing ranks_dict and hand_plus_board
    :return:
    """
    for rank in player.ranks_dict:
        if player.ranks_dict[rank] > 0:
            for card in player.hand_plus_board:

                if card.rank == rank:
                    player.hand_without_pairs.append(card)
                    break
    player.hand_without_pairs.sort(key=lambda card: card.rank)  # sort hand_without_pairs in place




def fill_ranks_dict(player):
    for card in player.hand_plus_board:
        for key in player.ranks_dict:
            if card.rank == key:
                player.ranks_dict[key] += 1

def fill_suits_dict(player):
    for card in player.hand_plus_board:
        for key in player.suits_dict:
            if card.suit == key:
                player.suits_dict[key] += 1

def fill_suits_and_ranks_dicts(player, table):

    fill_ranks_dict(player)
    fill_suits_dict(player)




