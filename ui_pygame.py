from dobblegame_pygame import DobbleGame
from ui_menu import Menu


def main():
    menu = Menu()
    game_parameters = menu.get_game_parameters()
    if game_parameters:
        computers, diff_level, num_of_symbols = game_parameters
        game = DobbleGame(computers, diff_level, num_of_symbols)
        game.run_game()


if __name__ == "__main__":
    main()
