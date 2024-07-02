from card import Card
from abc import ABC, abstractmethod


class Hand(ABC):
    def __init__(self):
        self._cards = []

    @property
    def cards(self):
        return self._cards

    @abstractmethod
    def draw(self, card):
        pass


class PocketHand(Hand):
    def __init__(self):
        super().__init__()

    @property
    def cards(self):
        return self.cards

    def draw(self, card):
        if not isinstance(card, Card):
            raise TypeError("Error: a card should be drawn")
        self.cards.append(card)


class CommunityHand(Hand):
    def __init__(self):
        super().__init__()

    @property
    def cards(self):
        return self.cards

    def draw(self, card):
        if not isinstance(card, Card):
            raise TypeError("Error: a card should be drawn")
        self.cards.append(card)
