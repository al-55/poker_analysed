class Card:

    """ Card class describes a single card"""

    RANKS = {1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 7, 7: 8,
             8: 9, 9: 10, 10: "JACK", 11: "QUEEN", 12: "KING", 13: "ACE"}

    SUITS = {1: "CLUBS", 2: "DIAMONDS", 3: "HEARTS", 4: "SPADES"}

    def __init__(self, rank, suit):
        self._validate(rank, Card.RANKS)
        self._validate(suit, Card.SUITS)
        self._rank = Card.RANKS[rank]
        self._suit = Card.SUITS[suit]

    @property
    def rank(self):
        return self._rank

    @property
    def suit(self):
        return self._suit

    def _validate(self, value, values):
        if value not in values:
            raise ValueError(f"VALUE ERROR: {value} is not in {values}.")

    def __eq__(self, other):
        if self.rank == other.rank and self.suit == other.suit:
            return True
        else:
            return False

    def __str__(self):
        return f"{self.rank} of {self.suit}"
