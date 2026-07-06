# from deck import Deck, Card, Table
SUITS = ["c", "d", "h", "s"]
class Player:
    def __init__(self, deck, table):

        self.seat_new_player(table)
        self.hand = []
        self.player_number = len(table.seated_players)
        self.hand_plus_board = []
        self.suits_dict = {key: 0 for key in SUITS}
        self.ranks_dict = {key: 0 for key in range(2, 15)}
        self.hand_without_pairs = []
        self.flush_cards_list = []
        self.ranks_list = []

        self.flush = False
        self.straight = False
        self.straight_flush = 0
        self.pairs = []
        self.two_pair = []
        self.trips = []
        self.full_house = []
        self.quads = []
        self.kickers = []
        self.hand_class = 0
        self.best_five = []
        self.kicker1 = 0
        self.kicker2 = 0
        self.kicker3 = 0
        self.kicker4 = 0
        self.kicker5 = 0
        self.wins = 0
        self.equity = 0
        # self.get_hand(deck)


    def __repr__(self):
        player_name = "Player " + str(self.player_number)
        return  player_name

    def print_hand(self):
        print(f"Player {self.player_number} hand: {self.hand}")

    def seat_new_player(self, table):
        table.seated_players.append(self)

    def deal(self, deck, number_of_cards=2):
        for num in range(number_of_cards):
            self.hand.append(deck.draw())


    def get_card(self, deck):
        rank = int(input("Please enter the rank of the card: "))
        while rank not in range(2, 15):
            rank = int(input("Please enter the rank of the card: "))

        suit = input("Please enter the suit of the card (c, d, h, s): ")
        new_card = deck.draw_specific(rank, suit)
        return new_card


    def get_hand(self, deck, number_of_cards=2):
        print(f"Enter Player {self.player_number}'s hand: ")
        for num in range(number_of_cards):
            print(f"Enter Card {num + 1} below...")
            card = None
            while card is None:
                card = self.get_card(deck)
            self.hand.append(card)

    def predetermined_hand(self, card1, card2, deck):
        self.hand.append(deck.draw_specific(card1.rank, card1.suit))
        self.hand.append(deck.draw_specific(card2.rank, card2.suit))

