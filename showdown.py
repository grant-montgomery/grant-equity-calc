
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


# def straight_checker(player, table):
#     """
#     Check if players have a straight
#     :param player: player object
#     :param table: table object (for board cards)
#     :return: int, 0 if no straight, otherwise highest straight card
#     """
#     high_card = 0
#     player.hand_plus_board.sort(key= lambda card : card.rank) # sort hand_plus_board in place
#     print(f"sorted hand = {player.hand_plus_board}")