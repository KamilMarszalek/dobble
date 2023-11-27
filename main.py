from game import Game
from input_with_timeout import input_with_timeout


def computer_wins():
    pass


if __name__ == "__main__":
    game = Game(3, 1, 8)
    game.create_cards()
    game.deal()

    while game.player.cards:
        print(game._middlecard.symbols())
        print(game.player.first_card().symbols())
        answer = input_with_timeout("Choose the common symbol: ", 15)
        if not answer:
            winner = game.choose_winner()
            symbol = winner.common_symbol(game._middlecard)
            print(f"{winner.name} has won this round. Common symbol: {symbol}")
            game.change_middle_card(winner.first_card())
            winner.remove_card(winner.first_card())
            if winner.verify_if_win():
                print(f"{winner.name} winning it all! It runs out of cards.")
                break
        if answer in game._middlecard.symbols():
            print("You're right")
            game.change_middle_card(game.player.first_card())
            game.player.remove_card(game.player.first_card())
            if game.player.verify_if_win():
                print("You win")
                break
        else:
            print("Wrong answer")
