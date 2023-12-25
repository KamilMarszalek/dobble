import random
from typing import Union, Optional
import pygame
from game import Game
from constants import WIDTH, HEIGHT, FPS, BACKGROUND, BLUE, WHITE
from player import Player
from computer import Computer


class DobbleGame:
    """
    Class DobbleGame represents a whole game of dobble in pygame.
    It uses methods of class Game to run the game in pygame.

    :param amount_of_computers: amount of computers participating in a game (from 1 to 3)
    :type amount_of_computers: int
    :param diff_level: difficulty level of the game (from 1 to 3)
    :type diff_level: int
    :param number_of_symbols: amount of symbols on a single card (from 3 to 8)
    :type number_of_symbols: int
    """

    def __init__(
        self,
        amount_of_computers: int,
        diff_level: int,
        number_of_symbols: int,
    ) -> None:
        """
        Initialize the DobbleGame class.

        :param amount_of_computers: amount of computers participating in a game
        :type amount_of_computers: int
        :param diff_level: difficulty level of the game
        :type diff_level: int
        :param number_of_symbols: amount of symbols on a single card
        :type number_of_symbols: int
        """
        pygame.font.init()
        self.game: Game = Game(
            amount_of_computers, diff_level, number_of_symbols
        )
        self.game.create_cards()
        self.game.deal()
        self.timeout: int = self.game.set_timeout()
        self.player_failed_event = pygame.USEREVENT + 1
        self.font = pygame.font.Font(None, 60)
        self.win = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Dobble")
        self.clock = pygame.time.Clock()
        pygame.time.set_timer(
            self.player_failed_event,
            random.randint(
                (self.timeout - 2) * 1000,
                (self.timeout + 2) * 1000,
            ),
        )
        self.game_is_running: bool = True

    def display_message(self, message: str, color: tuple) -> None:
        """
        Method display_message is responsible for
        showing the final result of the game.

        :param message: text which will be displayed
        :type message: str
        :param color: color of the message
        :type color: tuple
        """
        text_surface = self.font.render(message, True, color)
        text_rect = text_surface.get_rect()
        padding: int = 10
        text_rect.inflate_ip(padding * 2, padding * 2)
        text_rect.center: tuple = (WIDTH // 2, HEIGHT // 2)
        pygame.draw.rect(self.win, WHITE, text_rect)
        text_pos: tuple = (text_rect.left + padding, text_rect.top + padding)
        self.win.blit(text_surface, text_pos)
        pygame.display.update()
        pygame.time.wait(3000)

    def draw_card(
        self,
        player: Union[Player, Computer],
        x: int,
        y: int,
    ) -> None:
        """
        Draw a single card for given player.

        :param player: a player or computer player
        :type player: Union[Player, Computer]
        :param x: x-coordinate
        :type x: int
        :param y: y-coordinate
        :type y: int
        """
        if player:
            if player.first_card():
                player.first_card().draw_card(self.win, x, y)

    def draw_board(self):
        """
        Calls draw_card to draw cards for all players.
        """
        self.draw_card(self.game.player, 500, 700)
        self.game.middlecard.draw_card(self.win, 500, 375)
        self.draw_card(self.game.computer_player1, 500, 25)
        self.draw_card(self.game.computer_player2, 900, 375)
        self.draw_card(self.game.computer_player3, 100, 375)

    def player_failed(self) -> Optional[bool]:
        """
        Handles a situation when player failed.
        It uses methods from Game class.

        :return: True if the game has ended, otherwise None
        :rtype: Optional[bool]
        """
        self.game.player_failed()
        if self.game.verify_if_game_has_ended() is not None:
            self.display_message("YOU LOSE", BLUE)
            self.game_is_running = False
            return True

    def run_game(self) -> None:
        """
        Handles the game of Dobble.
        Handles events, draws cards
        """
        while self.game_is_running:
            self.clock.tick(FPS)
            self.win.fill(BACKGROUND)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_is_running = False
                elif event.type == pygame.MOUSEBUTTONUP:
                    timeout = self.game.set_timeout() * 1000
                    pygame.time.set_timer(self.player_failed_event, timeout)
                    mouse_pos = pygame.mouse.get_pos()
                    clicked_symbol = (
                        self.game.player.first_card().handle_click(mouse_pos)
                    )
                    if clicked_symbol is not None:
                        if clicked_symbol in self.game.middlecard.symbols:
                            self.game.change_middle_card(
                                self.game.player.first_card(),
                            )
                            self.game.player.remove_card(
                                self.game.player.first_card(),
                            )
                            win = "You win."
                            if self.game.verify_if_game_has_ended() == win:
                                self.display_message("YOU WIN!", BLUE)
                                self.game_is_running = False
                                break
                        else:
                            self.player_failed()
                            if not self.game_is_running:
                                break

                elif event.type == self.player_failed_event:
                    self.player_failed()
                    if not self.game_is_running:
                        break
            self.draw_board()
            pygame.display.update()
        pygame.quit()
