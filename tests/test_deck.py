import unittest
from card import Card
from deck import Deck


class DeckTest(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()
        self.card = Card(3, 4)

    def test_initial_deck_contains_52_cards(self):
        self.assertEqual(len(self.deck.cards), 52)

    def test_every_card_in_deck_is_instance_of_card(self):
        for card in self.deck.cards:
            self.assertIsInstance(card, Card)

    def test_card_removed_from_deck(self):
        self.deck.deal_card(self.card)
        self.assertNotIn(self.card, self.deck.cards)

    def test_card_added_to_dealt_deck(self):
        self.deck.deal_card(self.card)
        self.assertIn(self.card, self.deck.dealt_cards)



