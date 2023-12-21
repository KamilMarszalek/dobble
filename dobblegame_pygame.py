import pygame
from card import Card
from game import Game
from constants import WIDTH, HEIGHT, FPS, BACKGROUND, BLUE, WHITE
from player import Player
from computer import Computer
from typing import Union
import random


class DobbleGame:
    """Class DobbleGame represents a whole game of dobble in pygame.
    It uses methods of class Game to run the game in pygame.
    Contains attributes:
    :param amount_of_computers: amount of computers participating in a game (from 1 to 3)
    :type symbols: int
    :param diff_level: difficulty level of the game (from 1 to 3)
    :type: int
    :param number_of_symbols: amount of symbols on a single card (from 3 to 8)
    :type: int
    """

    def __init__(self, amount_of_computers, diff_level, number_of_symbols) -> None:
        pygame.font.init()
        self.game = Game(amount_of_computers, diff_level, number_of_symbols)
        self.game.create_cards()
        self.game.deal()
        self.timeout = self.game.set_timeout()
        self.player_failed_event = pygame.USEREVENT + 1
        self.font = pygame.font.Font(None, 60)
        self.win = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Dobble")
        self.clock = pygame.time.Clock()
        pygame.time.set_timer(
            self.player_failed_event,
            random.randint((self.timeout - 2) * 1000, (self.timeout + 2) * 1000),
        )
        self.run = True

    def display_message(self, message: str, color) -> None:
        """Method display_message is responsible for
        showing the final result of the game."""
        text_surface = self.font.render(message, True, color)
        text_rect = text_surface.get_rect()
        padding = 10
        text_rect.inflate_ip(padding * 2, padding * 2)
        text_rect.center = (WIDTH // 2, HEIGHT // 2)
        pygame.draw.rect(self.win, WHITE, text_rect)
        text_pos = (text_rect.left + padding, text_rect.top + padding)
        self.win.blit(text_surface, text_pos)
        pygame.display.update()
        pygame.time.wait(3000)

    def draw_card(self, player: Union[Player, Computer], x: int, y: int) -> None:
        """Draw a single card for given player."""
        if player:
            if player.first_card():
                player.first_card().draw_card(self.win, x, y)

    def run_game(self) -> None:
        """Handles the game of Dobble.
        Handles events, draws cards"""
        while self.run:
            self.clock.tick(FPS)
            self.win.fill(BACKGROUND)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                elif event.type == pygame.MOUSEBUTTONUP:
                    pygame.time.set_timer(
                        self.player_failed_event, self.game.set_timeout() * 1000
                    )
                    mouse_pos = pygame.mouse.get_pos()
                    clicked_symbol = self.game.player.first_card().handle_click(
                        mouse_pos
                    )
                    if clicked_symbol is not None:
                        print(
                            f"You clicked on symbol {clicked_symbol} on the player's card"
                        )
                        if clicked_symbol in self.game.middlecard.symbols:
                            self.game.change_middle_card(self.game.player.first_card())
                            self.game.player.remove_card(self.game.player.first_card())
                            if self.game.verify_if_game_has_ended() == "You win.":
                                self.display_message("YOU WIN!", BLUE)
                                self.run = False
                                break
                        else:
                            self.game.player_failed()
                            if self.game.verify_if_game_has_ended() is not None:
                                self.display_message("YOU LOSE", BLUE)
                                self.run = False
                                break
                elif event.type == self.player_failed_event:
                    self.game.player_failed()
                    if self.game.verify_if_game_has_ended() is not None:
                        self.display_message("YOU LOSE", BLUE)
                        self.run = False
                        break
            self.draw_card(self.game.player, 500, 700)
            self.game.middlecard.draw_card(self.win, 500, 375)
            self.draw_card(self.game.computer_player1, 500, 25)
            self.draw_card(self.game.computer_player2, 900, 375)
            self.draw_card(self.game.computer_player3, 100, 375)
            pygame.display.update()
        pygame.quit()
