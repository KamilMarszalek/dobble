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
        :raises EmptyNameError:
            If the name is empty
        """
        if not name:
            raise EmptyNameError("Computer player name cannot be empty")
        super().__init__(cards, name)

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
