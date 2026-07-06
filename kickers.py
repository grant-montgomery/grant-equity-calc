


def find_best_kickers(player):
    # first remove leftover pair cards from hand_without_pairs (I left single pair cards for straight check)
    try:
        if len(player.best_five) < 5 and player.hand_without_pairs:
            for card in player.best_five:
                for card_b in player.hand_without_pairs:
                    if card.rank == card_b.rank:
                        player.hand_without_pairs.remove(card_b)
            # fill in best_five with highest kickers until it has five cards
            try:
                player.kicker1 = player.hand_without_pairs[len(player.hand_without_pairs) - 1]
                player.kicker2 = player.hand_without_pairs[len(player.hand_without_pairs) - 2]
                player.kicker3 = player.hand_without_pairs[len(player.hand_without_pairs) - 3]
                player.kicker4 = player.hand_without_pairs[len(player.hand_without_pairs) - 4]
                player.kicker5 = player.hand_without_pairs[len(player.hand_without_pairs) - 5]
            except:
                print("...")
            slots = (5 - len(player.best_five))
            for _ in range(slots):

                kicker = player.hand_without_pairs.pop()
                player.best_five.append(kicker)
    except IndexError:
        print("...")

def find_biggest_pair(table, player1, player2):

    if player1.pairs[0] > player2.pairs[0]:
        print(f"Both players have hand class 1, but {player1} has best pair.")
        player1.wins += 1
    elif player1.pairs[0] < player2.pairs[0]:
        print(f"Both players have hand class 1, but {player1} has best pair.")
        player2.wins += 1
    else:
        print("Both players have the EXACT SAME PAIR; checking kickers now")
        if player1.kicker1.rank > player2.kicker1.rank:
            print(f"Player 1 has best kicker")
            player1.wins += 1
        elif player1.kicker1.rank < player2.kicker1.rank:
            print(f"Player 2 has best kicker")
            player2.wins += 1
        elif player1.kicker2.rank > player2.kicker2.rank:
            print(f"Player 1 has best kicker")
            player1.wins += 1
        elif player1.kicker2.rank < player2.kicker2.rank:
            print(f"Player 2 has best kicker")
            player2.wins += 1
        elif player1.kicker3.rank > player2.kicker3.rank:
            print(f"Player 1 has best kicker")
            player1.wins += 1
        elif player1.kicker3.rank < player2.kicker3.rank:
            print(f"Player 2 has best kicker")
            player2.wins += 1
        else:
            print("Both players have the exact same hand, including all of the kickers")
            player1.wins += .5
            player2.wins += .5