from game import Game


def main():
    computers = input("How many opponents would you like to have (1, 2 or 3)?: ")
    diff_level = input(
        "What difficulty level are you feeling like challenging (1, 2 or 3)?: "
    )
    num_of_symbols = input(
        "How many symbols on a single card would you like (from 3 to 8)?: "
    )
    game = Game(int(computers), int(diff_level), int(num_of_symbols))
    game.create_cards()
    game.deal()
    game.play()


if __name__ == "__main__":
    main()
