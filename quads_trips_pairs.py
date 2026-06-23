
def quad_checker(player):
    """
    Check if player has quads
    :param player: player object
    :return: int, rank of quads
    """
    for key in player.ranks_dict:
        if player.ranks_dict[key] == 4:
            print(f"Quad {key}'s detected for {player}!")
            player.quads = key
            if player.hand_class < 7:
                player.hand_class = 7
                for card in player.hand_plus_board:
                    if card.rank == key:
                        player.best_five.append(card)

            return key
    return None

def full_house_checker(player):
    """
    Check if player has a full house
    :param player: object, holds the player's hand
    :return: list of ints, player.full_house representing the full house values
    """
    trips_value = 0
    pair_value_a = 0

    for key in player.ranks_dict:  # find biggest trips
        if player.ranks_dict[key] == 3 and key > trips_value:
            trips_value = key
            # print(f"FH trips value set: {trips_value}")
    for key in player.ranks_dict: # find biggest pair (even if it's within smaller trips)
        if player.ranks_dict[key] >= 2 and trips_value != key > pair_value_a:
            pair_value_a = key
            # print(f"FH pair value set: {pair_value_a}")
    if trips_value > 0 and pair_value_a > 0:
        player.full_house.append(pair_value_a)
        player.full_house.append(trips_value)
        player.hand_class = 6
        pair_counter = 2
        for card in player.hand_plus_board:
            if card.rank == trips_value:
                player.best_five.append(card)

            if pair_counter > 0:
                if card.rank == pair_value_a:
                    player.best_five.append(card)
                    pair_counter -= 1
        return player.full_house
    return None


def trips_checker(player):
    """
    Check if player has trips
    :param player: player object
    :return: int, rank of trips
    """
    for key in player.ranks_dict:
        if player.ranks_dict[key] == 3:
            print(f"Trip {key}'s detected for {player}!")
            player.quads = key
            if player.hand_class < 3:
                player.hand_class = 3
                for card in player.hand_plus_board:
                    if card.rank == key:
                        player.best_five.append(card)

            return key
    return None

def two_pair_checker(player):
    """
    Check hand for two pairs
    :param player: player object containing hand info
    :return player.two_pair: list of ints representing rank of two pairs
    """
    high_pair = 0
    low_pair = 0
    for key in player.ranks_dict: # Find out if two pair exist, and which two are highest
        if player.ranks_dict[key] == 2:
            if not high_pair:
                high_pair = key
            if high_pair and not low_pair:
                if key > high_pair:
                    low_pair = high_pair
                    high_pair = key

            if high_pair and low_pair:
                if low_pair < key < high_pair:
                    low_pair = key
                elif key > high_pair:
                    low_pair = high_pair
                    high_pair = key


    if high_pair and low_pair:
        for card in player.hand_plus_board:
            if card.rank == high_pair:
                player.best_five.append(card)
            if card.rank == low_pair:
                player.best_five.append(card)
        player.two_pair.append(high_pair)
        player.two_pair.append(low_pair)
        player.hand_class = 2
        return player.two_pair
    return None

def pair_checker(player):
    pair = 0

    for key in player.ranks_dict:  # Find out if two pair exist, and which two are highest
        if player.ranks_dict[key] == 2:
            pair = key
    for card in player.hand_plus_board:
        if card.rank == pair:
            player.best_five.append(card)
            player.hand_class = 1