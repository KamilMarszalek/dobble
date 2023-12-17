from card import Card


class Player:
    """Class Player represents a user.
    Contains attributes:
    :param cards: computer's cards
    :type cards: list[Card]"""

    def __init__(self, cards: list[Card]) -> None:
        self.cards: list[Card] = cards

    def first_card(self) -> Card:
        """Returns first card"""
        return self.cards[0]

    def remove_card(self, card: Card) -> None:
        """Removes card from a list of cards"""
        self.cards.remove(card)

    def has_won(self) -> bool:
        """Returns True if no cards left"""
        return not self.cards