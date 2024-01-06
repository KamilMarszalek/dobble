from random import shuffle
import os

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
from pygame import Rect


class Card:
    """
    Class Card represents a single card in dobble.

    :param symbols: card's symbols
    :type symbols: list[str]
    """

    def __init__(self, symbols: list[str]) -> None:
        """
        Initialize the Card class.

        :param symbols: card's symbols
        :type symbols: list[str]
        """
        self._symbols: list[str] = symbols
        self.symbol_rects: list[tuple[str, Rect]] = []

    @property
    def symbols(self) -> list[str]:
        """
        Returns the symbols on the card.

        :return: symbols on the card
        :rtype: list[str]
        """
        return self._symbols

    def shuffle_symbols(self) -> None:
        """
        Shuffles symbols on a card.
        """
        shuffle(self._symbols)
