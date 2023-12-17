from pack import generate_pack
from card import Card
from exceptions import DiffLevelError, InvalidComputersAmount
from random import choice, randint
from player import Player
from computer import Computer
from input_with_timeout import input_with_timeout
from typing import Union, Optional

LEVELS: list[int] = [1, 2, 3]


class Game:
    """Class Game represents a whole game of dobble.
    It handle every element of the game.
    Contains attributes:
    :param amount_of_computers: amount of computers participating in a game.
    :type symbols: int
    :param diff_level: difficulty level of the game (from 1 to 3)
    :type: int
    :param number_of_symbols: amount of symbols on a single card (from 3 to 8)
    :type: int
    """

    def __init__(
        self, amount_of_computers: int, diff_level: int, number_of_symbols: int
    ) -> None:
        self._levels: list[int] = LEVELS
        if amount_of_computers > 3 or amount_of_computers < 1:
            text_error = "Amount of enemies must be between 1 and 3."
            raise InvalidComputersAmount(text_error)
        self._amount_of_computers: int = amount_of_computers
        if diff_level not in self._levels:
            text_error = "Difficulty level not found in the available options."
            raise DiffLevelError(text_error)
        self._diff_level: int = diff_level
        self._numbers_of_symbols: int = number_of_symbols
        self._pack: list[list[str]] = generate_pack(self._numbers_of_symbols)

    @property
    def amount_of_computers(self) -> int:
        return self._amount_of_computers

    def set_timeout(self) -> None:
        """According to difficulty level it sets right timeout"""
        if self.diff_level == 1:
            self._timeout: int = 25
        elif self.diff_level == 2:
            self._timeout: int = 15
        else:
            self._timeout: int = 5

    @amount_of_computers.setter
    def amount_of_computers(self, amount: int) -> None:
        self._amount_of_computers: int = amount

    @property
    def diff_level(self) -> int:
        return self._diff_level

    @diff_level.setter
    def diff_level(self, new_level: int) -> None:
        if new_level not in self._levels:
            text_error = "Difficulty level not found in the available options."
            raise DiffLevelError(text_error)
        self._diff_level: int = new_level

    @property
    def number_of_symbols(self) -> int:
        return self._numbers_of_symbols

    @number_of_symbols.setter
    def number_of_symbols(self, new_number_of_symbols: int) -> None:
        self._numbers_of_symbols: int = new_number_of_symbols

    def create_cards(self) -> None:
        """Creates a pack of already shuffled cards."""
        self._cards: list = []
        for card in self._pack:
            self._cards.append(Card(card))
        for card in self._cards:
            card.shuffle_symbols()

    def deal_one_player(
        self, number_of_cards: int, name: str = ""
    ) -> Union[Player, Computer]:
        """Deals cards to one player only"""
        cards: list[Card] = []
        for _ in range(number_of_cards):
            chosen_card: Card = choice(self._cards)
            cards.append(chosen_card)
            self._cards.remove(chosen_card)
        if not name:
            return Player(cards)
        else:
            return Computer(cards, name)

    def deal(self) -> None:
        """Deals cards between players."""
        middlecard: Card = choice(self._cards)
        self._middlecard: Card = middlecard
        self._cards.remove(middlecard)
        if self.amount_of_computers == 3:
            cards_per_person = len(self._cards) // 4
            self.comp1 = self.deal_one_player(cards_per_person, "Computer 1")
            self.comp2 = self.deal_one_player(cards_per_person, "Computer 2")
            self.comp3 = self.deal_one_player(cards_per_person, "Computer 3")
            self.player = self.deal_one_player(cards_per_person)
        elif self.amount_of_computers == 2:
            cards_per_person = len(self._cards) // 3
            self.comp1 = self.deal_one_player(cards_per_person, "Computer 1")
            self.comp2 = self.deal_one_player(cards_per_person, "Computer 2")
            self.player = self.deal_one_player(cards_per_person)
        else:
            cards_per_person = len(self._cards) // 2
            self.comp1 = self.deal_one_player(cards_per_person, "Computer 1")
            self.player = self.deal_one_player(cards_per_person)

    def change_middle_card(self, card: Card) -> None:
        """Enables to change the card on the table"""
        self._middlecard: Card = card

    def choose_winner(self) -> Computer:
        """Chooses winner of a single round between computer players
        if player did not answer right"""
        if self._amount_of_computers == 3:
            winner: Computer = choice([self.comp1, self.comp2, self.comp3])
        elif self._amount_of_computers == 2:
            winner: Computer = choice([self.comp1, self.comp2])
        else:
            winner: Computer = self.comp1
        return winner

    def player_failed(self) -> Optional[bool]:
        """Handles situation if player did not manage to find common symbol."""
        winner = self.choose_winner()
        symbol = winner.common_symbol(self._middlecard)
        print(f"{winner.name} has won this round. Common symbol: {symbol}")
        self.change_middle_card(winner.first_card())
        winner.remove_card(winner.first_card())
        if winner.has_won():
            print(f"{winner.name} winning it all! It runs out of cards.")
            return True

    def play(self) -> None:
        """Interface of the game"""
        while self.player.cards:
            print(self._middlecard.symbols)
            print(self.player.first_card().symbols)
            self.set_timeout()
            answer = input_with_timeout(
                "Choose the common symbol: ",
                randint(self._timeout - 2, self._timeout + 2),
            )
            if not answer:
                if self.player_failed():
                    break
            else:
                if (
                    answer in self._middlecard.symbols
                    and answer in self.player.first_card().symbols
                ):
                    print("You're right")
                    self.change_middle_card(self.player.first_card())
                    self.player.remove_card(self.player.first_card())
                    if self.player.has_won():
                        print("You win")
                        break
                else:
                    print("Wrong answer")
                    if self.player_failed():
                        break
