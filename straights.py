def straight_checker(player):
    """
    Check if player has a straight
    :param player: player object
    :param table: table object (for board cards)
    :return: int, 0 if no straight, otherwise highest straight card
    """
    high_card = 0

    print(f"{player} sorted hand = {player.hand_plus_board}")

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
                        if player.hand_class < 4:
                            player.hand_class = 4
    except IndexError:
        print("STRAIGHT CHECKER: Index out of range")