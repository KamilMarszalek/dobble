from game import Game
from dobblegame_pygame import DobbleGame


def main():
    computers = int(input("How many opponents would you like to have (1, 2 or 3)?: "))
    diff_level = int(
        input("What difficulty level are you feeling like challenging (1, 2 or 3)?: ")
    )
    num_of_symbols = int(
        input("How many symbols on a single card would you like (from 3 to 8)?: ")
    )
    game = DobbleGame(computers, diff_level, num_of_symbols)
    game.run_game()


if __name__ == "__main__":
    main()
