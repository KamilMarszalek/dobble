from card import Card
from player import Player
from exceptions import EmptyNameError


class Computer(Player):
    """
    Class Computer represents a computer player in the game.
    It inherits from class Player.

    :param name: computer's name(id)
    :type name: str
    :param cards: computer's cards
    :type cards: list[Card]
    """

    def __init__(self, cards: list[Card], name: str) -> None:
        """
        Initialize the Computer class.

        :param cards: computer's cards
        :type cards: list[Card]
        :param name: computer's name(id)
        :type name: str
        """
        if not name:
            raise EmptyNameError("Computer player name cannot be empty")
        super().__init__(cards)
        self._name: str = name

    @property
    def name(self) -> str:
        """
        Returns the name(id) of the computer player.

        :return: name(id) of the computer player
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, new_name: str) -> None:
        """
        Sets a new name(id) for the computer player.

        :param new_name: new name(id) for the computer player
        :type new_name: str
        """
        if not new_name:
            raise EmptyNameError("Computer player name cannot be empty")
        self._name = new_name

    def get_common_symbol(self, card: Card) -> str:
        """
        Finds the common symbol between the first card
        in computer's pack and the given card.

        :param card: card which is compared to the first card of the player
        :type card: Card
        :return: common symbol or None if there is no common symbol
        :rtype: str
        """
        first_card: Card = self.first_card()
        common_symbols = set(first_card.symbols) & set(card.symbols)
        return next(iter(common_symbols), None)
