class Card:

    """ Card class describes a single card"""

    __RANKS = {1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 7, 7: 8,
             8: 9, 9: 10, 10: "JACK", 11: "QUEEN", 12: "KING", 13: "ACE"}

    __SUITS = {1: "CLUBS", 2: "DIAMONDS", 3: "HEARTS", 4: "SPADES"}

    @staticmethod
    def __validate(value, values):
        if value not in values:
            raise ValueError(f"VALUE ERROR: {value} is not in {values}.")

    def __init__(self, rank, suit):
        type(self).__validate(rank, type(self).__RANKS)
        type(self).__validate(suit, type(self).__SUITS)
        self.__rank = Card.__RANKS[rank]
        self.__suit = Card.__SUITS[suit]

    def __repr__(self):
        return f"Card({self.__rank, self.__suit})"

    def __str__(self):
        return f"Rank: {self.__rank}, Suit: {self.__suit}"

    def __eq__(self, other):
        if self.__rank == other.__rank and self.__suit == other.__suit:
            return True
        else:
            return False

    @property
    def rank(self):
        return self.__rank

    @property
    def suit(self):
        return self.__suit
