from random import shuffle
from typing import Optional
import pygame
from exceptions import SymbolsError
from constants import RED, WHITE, CARD_WIDTH, CARD_HEIGHT


class Card:
    """Class Card represents a single card in dobble.
    Contains attributes:
    :param symbols: card's symbols
    :type symbols: list[str]"""

    def __init__(self, symbols: list[str]) -> None:
        self._symbols: list[str] = symbols
        self._symbol_rects = []

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

    def shuffle_symbols(self) -> None:
        """Shuffles symbols on a card."""
        shuffle(self._symbols)

    def draw_card(self, window, x, y) -> None:
        """Draws the card's symbols on the given window at the given position."""
        self._symbol_rects.clear()
        font = pygame.font.Font(None, 24)

        pygame.draw.rect(
            window, WHITE, (x, y, CARD_WIDTH, CARD_HEIGHT), border_radius=12
        )

        padding_beetween_symbols = CARD_HEIGHT / (len(self._symbols) + 2)
        for i, symbol in enumerate(self._symbols):
            symbol_x = 10 + x
            symbol_y = y + padding_beetween_symbols * (i + 1)

            text_surface = font.render(symbol, True, RED)

            window.blit(text_surface, (symbol_x, symbol_y))

            text_rect = text_surface.get_rect(topleft=(symbol_x, symbol_y))
            self._symbol_rects.append((symbol, text_rect))

    def handle_click(self, pos) -> Optional[str]:
        """Handles a click event. If symbol is clicked,
        returns the symbol. If no symbol is clicked, returns None"""
        for symbol, rect in self._symbol_rects:
            if rect.collidepoint(pos):
                return symbol
        return None
