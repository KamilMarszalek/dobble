from typing import Optional
import tkinter as tk
from constants import (
    MIN_COMPUTERS,
    MAX_COMPUTERS,
    MAX_DIFF_LEVEL,
    MIN_DIFF_LEVEL,
    MIN_SYMBOLS,
    MAX_SYMBOLS,
    RED_M,
    PINK,
    GREEN,
    YELLOW,
)


def rgb_to_hex(rgb):
    """
    Convert RGB color values to hexadecimal.

    :param rgb: Tuple of RGB color values.
    :type rgb: tuple[int, int, int]
    :return: Hexadecimal color string.
    :rtype: str
    """
    return "#%02x%02x%02x" % rgb


class Menu:
    """
    A class to represent the Dobble game menu.

    :ivar window: The Tkinter window for the menu.
    :ivar amount_of_computers: The number of computer players.
    :ivar diff_level: The difficulty level of the game.
    :ivar amount_of_symbols: The number of symbols on a single card.
    :ivar game_parameters: The parameters for the game.
    """

    def __init__(self) -> None:
        """
        Initialize the menu.

        :return: None
        """
        self.window = tk.Tk()
        self.window.title("Dobble menu")
        self.window.minsize(width=800, height=800)
        self.window.config(bg=YELLOW)
        self.amount_of_computers = MIN_COMPUTERS
        self.diff_level = MIN_DIFF_LEVEL
        self.amount_of_symbols = MIN_SYMBOLS
        self.game_parameters = None
        self.display_menu()

    def get_amount_of_computers(self, value: int) -> None:
        """
        Update the number of computers.

        :param value: The number of computer players.
        :type value: int
        :return: None
        """
        self.amount_of_computers = int(value)

    def get_diff_level(self, value: int) -> None:
        """
        Update the difficulty level.

        :param value: The difficulty level of the game.
        :type value: int
        :return: None
        """
        self.diff_level = int(value)

    def get_amount_of_symbols(self, value: int) -> None:
        """
        Update the number of symbols.

        :param value: The number of symbols on a single card.
        :type value: int
        :return: None
        """
        self.amount_of_symbols = int(value)

    def start_game(self) -> None:
        """
        Close the window of menu and start dobble game.

        :return: None
        """
        self.game_parameters = (
            self.amount_of_computers,
            self.diff_level,
            self.amount_of_symbols,
        )
        self.window.destroy()

    def get_game_parameters(self) -> Optional[tuple[int, int, int]]:
        """
        Fetch game parameters.

        :return: A tuple containing the number of computers,
                 difficulty level,
                 and number of symbols.
                 Returns None if the parameters could not be fetched.
        :rtype: Optional[tuple[int, int, int]]
        """
        return self.game_parameters

    def display_menu(self) -> None:
        """
        Display the game menu.

        :return: None
        """
        computers_label = tk.Label(
            text="How many opponents would you like to play with?",
            font=("Arial", 20, "normal"),
            bg=YELLOW,
            fg=GREEN,
        )
        computers_label.pack(pady=20)

        computers = tk.Scale(
            from_=MIN_COMPUTERS,
            to=MAX_COMPUTERS,
            command=self.get_amount_of_computers,
            orient="horizontal",
            bg=YELLOW,
            fg=RED_M,
            highlightthickness=0,
            troughcolor=PINK,
            sliderrelief="flat",
        )
        computers.pack(pady=20)
        diff_level_text = (
            "What difficulty level do you feel like challenging yourself?"
        )
        diff_level_label = tk.Label(
            text=diff_level_text,
            font=("Arial", 20, "normal"),
            bg=YELLOW,
            fg=GREEN,
        )
        diff_level_label.pack(pady=20)

        diff_level = tk.Scale(
            from_=MIN_DIFF_LEVEL,
            to=MAX_DIFF_LEVEL,
            command=self.get_diff_level,
            orient="horizontal",
            bg=YELLOW,
            fg=RED_M,
            highlightthickness=0,
            troughcolor=PINK,
            sliderrelief="flat",
        )
        diff_level.pack(pady=20)

        amount_of_symbols_label = tk.Label(
            text="How many symbols on a card?",
            font=("Arial", 20, "normal"),
            bg=YELLOW,
            fg=GREEN,
        )
        amount_of_symbols_label.pack(pady=20)

        amount_of_symbols = tk.Scale(
            from_=MIN_SYMBOLS,
            to=MAX_SYMBOLS,
            command=self.get_amount_of_symbols,
            orient="horizontal",
            bg=YELLOW,
            fg=RED_M,
            highlightthickness=0,
            troughcolor=PINK,
            sliderrelief="flat",
        )
        amount_of_symbols.pack(pady=20)
        start_button = tk.Button(
            text="START", font=("Arial", 20, "normal"), command=self.start_game
        )
        start_button.config(bg="white", fg=RED_M, highlightthickness=0)
        start_button.pack(pady=20)
        self.window.mainloop()
