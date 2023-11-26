from random import shuffle
from exceptions import SymbolsError


class Card:
    def __init__(self, symbols):
        self._symbols = symbols

    def symbols(self):
        return self._symbols

    def set_symbols(self, symbols):
        if len(symbols) != len(self.symbols()):
            raise SymbolsError(
                "Length of new symbols is not equal to  the previous one."
            )
        self._symbols = symbols

    def shuffle_symbols(self):
        shuffle(self._symbols)
