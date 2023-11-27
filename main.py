from game import Game


if __name__ == "__main__":
    game = Game(3, 1, 8)
    game.create_cards()
    game.deal()

    while game.player.cards:
        print(game._middlecard.symbols())
        print(game.player.first_card().symbols())
        answer = input("Choose the common symbol: ")
        if answer in game._middlecard.symbols():
            print("You're right")
            game.change_middle_card(game.player.first_card())
            game.player.remove_card(game.player.first_card())
            if game.player.verify_if_win():
                print("You win")
                break
        else:
            print("Wrong answer")
