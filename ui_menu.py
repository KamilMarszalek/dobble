import tkinter as tk
from constants import (
    MIN_COMPUTERS,
    MAX_COMPUTERS,
    MAX_DIFF_LEVEL,
    MIN_DIFF_LEVEL,
    MIN_SYMBOLS,
    MAX_SYMBOLS,
)


def rgb_to_hex(rgb):
    return "#%02x%02x%02x" % rgb


class Menu:
    """A class to represent the Dobble game menu."""

    def __init__(self) -> None:
        """Initialize the menu."""
        self.window = tk.Tk()
        self.window.title("Dobble menu")
        self.window.minsize(width=800, height=800)
        self.amount_of_computers = MIN_COMPUTERS
        self.diff_level = MIN_DIFF_LEVEL
        self.amount_of_symbols = MIN_SYMBOLS
        self.display_menu()

    def get_amount_of_computers(self, value):
        """Update the number of computers."""
        self.amount_of_computers = int(value)

    def get_diff_level(self, value):
        """Update the difficulty level."""
        self.diff_level = int(value)

    def get_amount_of_symbols(self, value):
        """Update the number of symbols."""
        self.amount_of_symbols = int(value)

    def start_game(self):
        self.game_parameters = (
            self.amount_of_computers,
            self.diff_level,
            self.amount_of_symbols,
        )
        self.window.destroy()

    def get_game_parameters(self):
        return self.game_parameters

    def display_menu(self):
        """Display the game menu."""
        computers_label = tk.Label(
            text="How many opponents would you like to play with?",
            font=("Arial", 20, "normal"),
        )
        computers_label.pack(pady=20)

        computers = tk.Scale(
            from_=MIN_COMPUTERS,
            to=MAX_COMPUTERS,
            command=self.get_amount_of_computers,
            orient="horizontal",
        )
        computers.pack(pady=20)

        diff_level_label = tk.Label(
            text="What difficulty level do you feel like challenging yourself?",
            font=("Arial", 20, "normal"),
        )
        diff_level_label.pack(pady=20)

        diff_level = tk.Scale(
            from_=MIN_DIFF_LEVEL,
            to=MAX_DIFF_LEVEL,
            command=self.get_diff_level,
            orient="horizontal",
        )
        diff_level.pack(pady=20)

        amount_of_symbols_label = tk.Label(
            text="How many symbols on a card?",
            font=("Arial", 20, "normal"),
        )
        amount_of_symbols_label.pack(pady=20)

        amount_of_symbols = tk.Scale(
            from_=MIN_SYMBOLS,
            to=MAX_SYMBOLS,
            command=self.get_amount_of_symbols,
            orient="horizontal",
        )
        amount_of_symbols.pack(pady=20)
        start_button = tk.Button(
            text="START", font=("Arial", 20, "normal"), command=self.start_game
        )
        start_button.pack(pady=20)
        self.window.mainloop()
