from card import Card


class Deck:

    """ Deck class describes a deck of cards """

    __RANKS = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)
    __SUITS = (1, 2, 3, 4)

    def __init__(self):
        self.__cards = [Card(rank, suit) for rank in type(self).__RANKS for suit in type(self).__SUITS]
        self.__dealt_cards = []

    def __str__(self):
        return f"Deck: {self.cards}"

    @property
    def cards(self):
        return self.__cards

    @property
    def dealt_cards(self):
        return self.__dealt_cards

    def deal_card(self, card):
        if card not in self.cards:
            raise ValueError(f"{card} is not in {self.cards}")
        self.cards.remove(card)
        self.dealt_cards.append(card)
