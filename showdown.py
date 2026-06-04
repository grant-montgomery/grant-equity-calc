
def determine_hand_strength(player, player2, table):
    for person in table.seated_players:
        # prepping properties to make hand comparison easier
        combine_hand_and_board(person, table)
        fill_suits_and_ranks_dicts(person, table)
        remove_pairs(person)

        # determining if player has specific hand classes
        straight_checker(person, table)



def combine_hand_and_board(player, table):
    # first combine players' hand and board into hand_plus_board

    for cards in player.hand:
        player.hand_plus_board.append(cards)
    for card in table.board:
        player.hand_plus_board.append(card)
    print(f"{player}'s hand combined successfully into {player.hand_plus_board}")


def remove_pairs(player):
    start_point = 1
    player.hand_without_pairs = player.hand_plus_board.copy()
    for card in player.hand_without_pairs:
        try:

            for index in range(start_point, len(player.hand_without_pairs) - 1):
                if card.rank == player.hand_without_pairs[index].rank:
                    pair_card = player.hand_without_pairs[index]

                    player.hand_without_pairs.remove(player.hand_without_pairs[index])

            start_point += 1
        except IndexError:
            print("PAIR REMOVER: card index out of range")


def straight_checker(player, table):
    """
    Check if player has a straight
    :param player: player object
    :param table: table object (for board cards)
    :return: int, 0 if no straight, otherwise highest straight card
    """
    high_card = 0
    player.hand_without_pairs.sort(key= lambda card : card.rank) # sort hand_plus_board in place
    print(f"{player} sorted hand = {player.hand_plus_board}")
    # next step: make player.hand_with_pairs_removed so that straights will show even
    # if there is a pair within the "straight cards"
    try:
        for index in range(0, 3):
            continuous = True
            for num in range(1, 5):
                if continuous:
                    if player.hand_without_pairs[index].rank != player.hand_without_pairs[index + num].rank - num:
                        continuous = False
                    if num == 4 and continuous == True:
                        player.straight = player.hand_without_pairs[num + index]
                        high_card = player.hand_without_pairs[num + index].rank
                        print(f'{player} has a {player.straight} high straight')
                        print(high_card)
    except IndexError:
        print("STRAIGHT CHECKER: Index out of range")

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




