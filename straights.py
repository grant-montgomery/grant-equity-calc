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
                straight_list = []
                if continuous:
                    if player.hand_without_pairs[index].rank != player.hand_without_pairs[index + num].rank - num:
                        continuous = False
                    if num == 4 and continuous == True:
                        player.straight = player.hand_without_pairs[num + index]
                        # populate straight list for making best five card hand
                        for back_cycler in range(0, 5):
                            straight_list.append(player.hand_without_pairs[num + index - back_cycler])

                        high_card = player.hand_without_pairs[num + index].rank
                        print(f'{player} has a {player.straight} high straight')
                        print(high_card)
                        if player.hand_class < 4:
                            player.hand_class = 4
                        player.best_five = straight_list
    except IndexError:
        print("STRAIGHT CHECKER: Index out of range")


def flush_checker(player):
    """
    Check hand for a flush
    :param player: player object containing hand info
    :return: player.flush, int representing how high the flush is
    """
    flush_suit = ""
    flush_cards = []
    flush_check = False
    try:
        for suit in player.suits_dict:
            if player.suits_dict[suit] >= 5:
                flush_suit = suit
                flush_check = True
        if flush_check:
            for card in player.hand_plus_board:
                if card.suit == flush_suit:
                    flush_cards.append(card)
            for index in reversed(range(len(flush_cards) - 4, len(flush_cards))):
                player.best_five.append(flush_cards[index]) # find highest five flush cards
            player.best_five.sort(key=lambda card: card.rank)  # sort by rank
            player.flush = player.best_five[4]
            print(f'{player} has a flush: {player.flush} high')
    except IndexError:
        print("Index error during flush determination")
