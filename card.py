from random import shuffle
from exceptions import SymbolsError


class Card:
    """Class Card represents a single card in dobble.
    Contains attributes:
    :param symbols: card's symbols
    :type symbols: list[str]"""

    def __init__(self, symbols: list[str]) -> None:
        self._symbols: list[str] = symbols

    @property
    def symbols(self) -> list[str]:
        """Returns the symbols on the card."""
        return self._symbols

    @symbols.setter
    def symbols(self, symbols: list[str]) -> None:
        """Sets the symbols on the card, ensuring the new symbols have the same length as the old ones.
        Raises:
        SymbolError: If the length of the new symbols is not equal to the length of the old ones.
        """
        if len(symbols) != len(self._symbols):
            raise SymbolsError(
                "Length of new symbols is not equal to the previous one."
            )
        self._symbols = symbols

    def shuffle_symbols(self):
        """Shuffles symbols on a card."""
        shuffle(self._symbols)
