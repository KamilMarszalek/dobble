from dobblegame_pygame import DobbleGame
from ui_menu import Menu


def main():
    """Handle Dobble game in a pygame environment.
    Uses class Menu() to fetch data. Menu() is
    displayed from tkinter module.

    """
    menu = Menu()
    game_parameters = menu.get_game_parameters()
    if game_parameters:
        computers, diff_level, num_of_symbols = game_parameters
        game = DobbleGame(int(computers), int(diff_level), int(num_of_symbols))
        game.run_game()


if __name__ == "__main__":
    main()
