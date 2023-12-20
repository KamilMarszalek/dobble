from card import Card
from player import Player
from exceptions import EmptyNameError


class Computer(Player):
    """Class Computer represents a computer.
    It inherits from class Player.
    Contains attributes:
    :param name: computer's name(id)
    :type name: str
    :param cards: computer's cards
    :type cards: list[Card]"""

    def __init__(self, cards: list[Card], name: str) -> None:
        if not name:
            raise EmptyNameError("Name cannot be empty")
        super().__init__(cards)
        self._name: str = name

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, new_name: str) -> None:
        if not new_name:
            raise EmptyNameError("Name cannot be empty")
        self._name = new_name

    def common_symbol(self, card: Card) -> str:
        """Finds the common symbol between
        First card in computer's pack and given card."""
        first_card: Card = self.first_card()
        for symbol in first_card.symbols:
            if symbol in card.symbols:
                return symbol
