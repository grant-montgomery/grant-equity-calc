
def showdown(player1, player2, table):

    combine_hand_and_board(player1, table)


def combine_hand_and_board(player, table):
    # first combine players' hand and board into hand_plus_board
    for player in table.seated_players:

        for cards in player.hand:
            player.hand_plus_board.append(cards)
        for card in table.board:
            player.hand_plus_board.append(card)
        print(f"{player}'s hand combined successfully into {player.hand_plus_board}")


def straight_checker(player, table):
    """
    Check if player has a straight
    :param player: player object
    :param table: table object (for board cards)
    :return: int, 0 if no straight, otherwise highest straight card
    """
    high_card = 0
    player.hand_plus_board.sort(key= lambda card : card.rank) # sort hand_plus_board in place
    print(f"sorted hand = {player.hand_plus_board}")
    # check if there are five cards in a row
    # choose first straight card
    # check if index = index +1
    # add 1 to index
    # check again until we get to index = original index + 4
    # if all are true; straightHighCard = card indexed at index+4
    # choose second straight card
    # run index check again

    for index in range(0, 3):
        continuous = True
        for num in range(1, 5):
            if continuous == True:
                if player.hand_plus_board[index].rank != player.hand_plus_board[index + num].rank - num:
                    continuous = False
                if num == 4 and continuous == True:
                    player.straight = player.hand_plus_board[num]
                    high_card = player.hand_plus_board[num].rank
                    print(f'{player} has a {player.straight} high straight')
                    print(high_card)



