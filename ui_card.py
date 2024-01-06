from typing import Union, Optional
import pygame
from constants import WHITE, CARD_HEIGHT, CARD_WIDTH, RED
from card import Card


class UICard:
    """
    Class UICard is responsible for drawing the card
    and handling player clicking.

    """

    @staticmethod
    def draw_card(
        card: Card,
        window,
        x: Union[float, int],
        y: Union[float, int],
        player_name: str = None,
        cards_left: int = None,
    ) -> None:
        """
        Draws the card's symbols on the given window at the given position.

        :param card: The card to be drawn.
        :type card: Card
        :param window: The pygame window where the card will be drawn.
        :param x: The x-coordinate where the card will be drawn.
        :type x: Union[float, int]
        :param y: The y-coordinate where the card will be drawn.
        :type y: Union[float, int]
        """
        card.symbol_rects.clear()
        font = pygame.font.Font(None, 25)

        pygame.draw.rect(
            window, WHITE, (x, y, CARD_WIDTH, CARD_HEIGHT), border_radius=12
        )
        if player_name and cards_left:
            name_surface = font.render(
                f"{player_name}: {cards_left} cards left", True, WHITE
            )
            window.blit(name_surface, (x, y - name_surface.get_height()))

        padding_beetween_symbols = CARD_HEIGHT / (len(card.symbols) + 2)
        for i, symbol in enumerate(card.symbols):
            symbol_x = 10 + x
            symbol_y = y + padding_beetween_symbols * (i + 1)

            text_surface = font.render(symbol, True, RED)

            window.blit(text_surface, (symbol_x, symbol_y))

            text_rect = text_surface.get_rect(topleft=(symbol_x, symbol_y))
            card.symbol_rects.append((symbol, text_rect))

    @staticmethod
    def handle_click(card: Card, pos: tuple[int, int]) -> Optional[str]:
        """
        Handles a click event. If a symbol is clicked, returns the symbol.
        If no symbol is clicked, returns None.

        :param card: The card where the click event will be handled.
        :type card: Card
        :param pos: The position of the cursor when the click was done.
        :type pos: tuple[int, int]
        :return: The clicked symbol, or None if no symbol was clicked.
        :rtype: Optional[str]
        """
        for symbol, rect in card.symbol_rects:
            if rect.collidepoint(pos):
                return symbol
        return None
