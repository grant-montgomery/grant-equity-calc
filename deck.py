import random

SUITS = [ "c", "d", "h", "s"]
RANKS = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

class Deck:
    def __init__(self):
        self.cards = []
        self.build()


    def __repr__(self):
        return str(self.cards)

    def build(self):
        for suit in SUITS:
            for num in range(2, 15):  # 2-10 as shown, 11-14 are Jacks-Aces
                card = Card(suit, num)
                self.cards.append(card)

    def shuffle_up(self):
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop()

    def draw_specific(self, rank, suit):
        card_found = False
        for card in self.cards:
            if card_found == False:
                if card.rank == rank and card.suit == suit:
                    card_found = True
                    self.cards.remove(card)
                    return card
            else:
                print("card has already been drawn")
                break
        return None

    # def seat_another_player(self):
    #     self.number_of_players += 1

    def get_flop(self, table):

        for num in range(3):
            rank = int(input("Enter the rank of the next board card: "))
            suit = input("Enter the suit of the next board card: ")
            table.board.append(self.draw_specific(rank, suit))

    def get_turn(self, table):

        rank = int(input("Enter the rank of the next board card: "))
        suit = input("Enter the suit of the next board card: ")
        table.board.append(self.draw_specific(rank, suit))

    def deal_full_board(self, table):
        for num in range(1, 6):
            card = self.draw()

            table.board.append(card)

    def deal_specific_board(self, table): # for testing
        table.board.append(self.draw_specific(11, "c"))
        table.board.append(self.draw_specific(10, "h"))
        table.board.append(self.draw_specific(3, "s"))
        table.board.append(self.draw_specific(4, "s"))
        table.board.append(self.draw_specific(5, "s"))



class Table:
    def __init__(self):
        self.seated_players = []
        self.tied_players = []
        self.board = []
        self.skipped_runs = 0

class Card:
    def __init__(self, suit, rank):
      self.suit = suit
      self.rank = rank

    def __repr__(self):
        card_value = str(self.rank) + str(self.suit)
        return card_value