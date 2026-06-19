


def find_best_kickers(player):
    # first remove leftover pair cards from hand_without_pairs (I left single pair cards for straight check)
    try:
        if len(player.best_five) < 5 and player.hand_without_pairs:
            for card in player.best_five:
                for card_b in player.hand_without_pairs:
                    if card.rank == card_b.rank:
                        player.hand_without_pairs.remove(card_b)
            # fill in best_five with highest kickers until it has five cards
            slots = (5 - len(player.best_five))
            for _ in range(slots):

                kicker = player.hand_without_pairs.pop()
                player.best_five.append(kicker)
    except IndexError:
        print("index error while kickering")