from dobblegame_pygame import DobbleGame
from ui_menu import Menu


def main() -> None:
    """
    Handle Dobble game in a pygame environment.

    This function sets up and executes a pygame-based version of the
    Dobble (Spot It!) game.
    It uses the Menu class to fetch game parameters.
    The Menu is displayed using the tkinter module.

    :return: None
    """
    menu = Menu()
    game_parameters = menu.get_game_parameters()
    if game_parameters:
        computers, diff_level, num_of_symbols = game_parameters
        game = DobbleGame(int(computers), int(diff_level), int(num_of_symbols))
        game.run_game()


if __name__ == "__main__":
    main()
