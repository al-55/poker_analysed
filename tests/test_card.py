import unittest
from card import Card


class CardTest(unittest.TestCase):
    def setUp(self):
        self.card = Card(1, 2)

    def test_card_creation(self):
        self.assertIsInstance(self.card, Card, f"Expected {self.card} to be an instance of the Card class")

    def test_create_card_raise_exception(self):
        with self.assertRaises(ValueError):
            self.first_card = Card(14, 3)
            self.second_card = Card(8, 5)
            self.third_card = Card(15, 8)

    def test_card_has_right_rank(self):
        self.assertEqual(Card(2, 3).rank, 3)

    def test_card_has_right_suit(self):
        self.assertEqual(Card(8, 1).suit, "CLUBS")


if __name__ == '__main__':
    unittest.main()
