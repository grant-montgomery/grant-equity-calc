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
        remove_pairs(person)

        # determining if player has specific hand classes
        if person.hand_class < 8:
            quad_checker(person)
        if person.hand_class < 7:
            full_house_checker(person)
        if person.hand_class < 5:
            straight_checker(person)
        if person.hand_class < 4:
            trips_checker(person)
        find_best_kickers(person)


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


def remove_pairs(player):
    start_point = 0
    player.hand_without_pairs = player.hand_plus_board.copy()
    for card in player.hand_without_pairs:
        try:

            for index in range(start_point, len(player.hand_without_pairs) - 1):
                if card.rank == player.hand_without_pairs[index +1].rank:
                    pair_card = player.hand_without_pairs[index + 1]

                    player.hand_without_pairs.remove(pair_card)

            start_point += 1
        except IndexError:
            print("PAIR REMOVER: card index out of range")
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




