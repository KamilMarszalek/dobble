from pack import generate_pack
from card import Card
from exceptions import DiffLevelError, InvalidEnemyAmount
from random import choice
from player import Player
from computer import Computer


class Game:
    def __init__(self, amount_of_computers, diff_level, number_of_symbols):
        self.__levels = [1, 2, 3]
        if amount_of_computers > 3 or amount_of_computers < 1:
            text_error = "Amount of enemies must be between 1 and 3."
            raise InvalidEnemyAmount(text_error)
        self._amount_of_computers = amount_of_computers
        if diff_level not in self.__levels:
            text_error = "Difficulty level not found in the available options."
            raise DiffLevelError(text_error)
        self._diff_level = diff_level
        self._numbers_of_symbols = number_of_symbols
        self._pack = generate_pack(self._numbers_of_symbols)

    def amount_of_computers(self):
        return self._amount_of_computers

    def set_amount_of_computers(self, amount):
        self._amount_of_computers = amount

    def diff_level(self):
        return self._diff_level

    def set_diff_level(self, new_level):
        self._diff_level = new_level

    def number_of_symbols(self):
        return self._numbers_of_symbols

    def set_number_of_symbols(self, new_number_of_symbols):
        self._numbers_of_symbols = new_number_of_symbols

    def create_cards(self):
        self._cards = []
        for card in self._pack:
            self._cards.append(Card(card))
        for card in self._cards:
            card.shuffle_symbols()

    def deal(self):
        middlecard = choice(self._cards)
        self._middlecard = middlecard
        self._cards.remove(middlecard)
        player_cards = []
        if self._amount_of_computers == 3:
            comp1_cards = []
            comp2_cards = []
            comp3_cards = []
            for i in range(14):
                chosen_card = choice(self._cards)
                player_cards.append(chosen_card)
                self._cards.remove(chosen_card)
            for i in range(14):
                chosen_card = choice(self._cards)
                comp1_cards.append(chosen_card)
                self._cards.remove(chosen_card)
            for i in range(14):
                chosen_card = choice(self._cards)
                comp2_cards.append(chosen_card)
                self._cards.remove(chosen_card)
            for i in range(14):
                chosen_card = choice(self._cards)
                comp3_cards.append(chosen_card)
                self._cards.remove(chosen_card)
            player = Player(player_cards)
            comp1 = Computer(comp1_cards)
            comp2 = Computer(comp2_cards)
            comp3 = Computer(comp3_cards)
            return (player, comp1, comp2, comp3)
