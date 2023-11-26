from game import Game
from player import Player
from computer import Computer
from card import Card
from pack import generate_pack


game = Game(3, 2, 8)
# print(game._pack)
game.create_cards()
# print(game._cards)
# for card in game._cards:
#     print(card._symbols)
game.create_cards()
for card in game.deal()[0].cards:
    print(card._symbols)
