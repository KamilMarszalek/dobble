from pack import generate_pack
from card import Card
from typing import Union, Optional
from random import choice, randint
from exceptions import DiffLevelError, InvalidComputersAmount, SymbolsError
from player import Player
from computer import Computer
from input_with_timeout import input_with_timeout
from constants import (
    MAX_COMPUTERS,
    MIN_COMPUTERS,
    MIN_SYMBOLS,
    MAX_SYMBOLS,
    LEVELS,
)


class Game:
    """
    Class Game represents a whole game of dobble.
    It handles every element of the game.
    Calling play method enables to play in the terminal.

    :param amount_of_computers: amount of computers participating in a game
                                (from 1 to 3)
    :type amount_of_computers: int
    :param diff_level: difficulty level of the game (from 1 to 3)
    :type diff_level: int
    :param number_of_symbols: amount of symbols on a single card (from 3 to 8)
    :type number_of_symbols: int
    """

    def __init__(
        self, amount_of_computers: int, diff_level: int, number_of_symbols: int
    ) -> None:
        """
        Initialize the Game class.

        :param amount_of_computers: amount of computers participating in a game
        :type amount_of_computers: int
        :param diff_level: difficulty level of the game
        :type diff_level: int
        :param number_of_symbols: amount of symbols on a single card
        :type number_of_symbols: int
        """
        self._levels: list[int] = LEVELS
        if (
            amount_of_computers > MAX_COMPUTERS
            or amount_of_computers < MIN_COMPUTERS
        ):
            text_error = "Amount of enemies must be between 1 and 3."
            raise InvalidComputersAmount(text_error)
        self._amount_of_computers: int = amount_of_computers
        if diff_level not in self._levels:
            text_error = "Difficulty level not found in the available options."
            raise DiffLevelError(text_error)
        if number_of_symbols > MAX_SYMBOLS or number_of_symbols < MIN_SYMBOLS:
            text_error = "Number of symbols must be between 3 and 8."
            raise SymbolsError(text_error)
        self._diff_level: int = diff_level
        self._numbers_of_symbols: int = number_of_symbols
        self._pack: list[list[str]] = generate_pack(self._numbers_of_symbols)
        self.player = None
        self.computer_player1 = None
        self.computer_player2 = None
        self.computer_player3 = None

    @property
    def amount_of_computers(self) -> int:
        """
        Return amount of computer players.

        :return: amount of computer players
        :rtype: int
        """
        return self._amount_of_computers

    def set_timeout(self) -> int:
        """
        According to difficulty level it sets right timeout.

        :return: timeout value
        :rtype: int
        """
        if self.diff_level == 1:
            self._timeout: int = 25
        elif self.diff_level == 2:
            self._timeout: int = 15
        else:
            self._timeout: int = 5
        return self._timeout

    @amount_of_computers.setter
    def amount_of_computers(self, amount: int) -> None:
        """
        Set the amount of computer players.

        :param amount: new amount of computer players
        :type amount: int
        """
        self._amount_of_computers: int = amount

    @property
    def diff_level(self) -> int:
        """
        Get the difficulty level of the game.

        :return: difficulty level of the game
        :rtype: int
        """
        return self._diff_level

    @diff_level.setter
    def diff_level(self, new_level: int) -> None:
        """
        Set the difficulty level of the game.

        :param new_level: new difficulty level of the game
        :type new_level: int
        """
        if new_level not in self._levels:
            text_error = "Difficulty level not found in the available options."
            raise DiffLevelError(text_error)
        self._diff_level: int = new_level

    @property
    def number_of_symbols(self) -> int:
        """
        Get the number of symbols on a single card.

        :return: number of symbols on a single card
        :rtype: int
        """
        return self._numbers_of_symbols

    @number_of_symbols.setter
    def number_of_symbols(self, new_number_of_symbols: int) -> None:
        """
        Set the number of symbols on a single card.

        :param new_number_of_symbols: new number of symbols on a single card
        :type new_number_of_symbols: int
        """
        self._numbers_of_symbols: int = new_number_of_symbols

    def create_cards(self) -> None:
        """
        Creates a pack of already shuffled cards.
        """
        self._cards: list = []
        for card in self._pack:
            self._cards.append(Card(card))
        for card in self._cards:
            card.shuffle_symbols()

    def deal_one_player(
        self, number_of_cards: int, name: str = ""
    ) -> Union[Player, Computer]:
        """
        Deals cards to one player only.

        :param number_of_cards: amount of cards to be given to a player
        :type number_of_cards: int
        :param name: it is given to distinguish computer player
                    from real player
        :type name: str
        :return: Player or Computer object
        :rtype: Union[Player, Computer]
        """
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
        """
        Deals cards between players.
        """
        middlecard: Card = choice(self._cards)
        self.middlecard: Card = middlecard
        self._cards.remove(middlecard)
        if self.amount_of_computers == 3:
            cards_per_person = len(self._cards) // 4
            self.computer_player1 = self.deal_one_player(
                cards_per_person,
                "Computer 1",
            )
            self.computer_player2 = self.deal_one_player(
                cards_per_person,
                "Computer 2",
            )
            self.computer_player3 = self.deal_one_player(
                cards_per_person,
                "Computer 3",
            )
            self.player = self.deal_one_player(cards_per_person)
            self.comps = [
                self.computer_player1,
                self.computer_player2,
                self.computer_player3,
            ]
        elif self.amount_of_computers == 2:
            cards_per_person = len(self._cards) // 3
            self.computer_player1 = self.deal_one_player(
                cards_per_person,
                "Computer 1",
            )
            self.computer_player2 = self.deal_one_player(
                cards_per_person,
                "Computer 2",
            )
            self.player = self.deal_one_player(cards_per_person)
            self.comps = [self.computer_player1, self.computer_player2]
        else:
            cards_per_person = len(self._cards) // 2
            self.computer_player1 = self.deal_one_player(
                cards_per_person,
                "Computer 1",
            )
            self.player = self.deal_one_player(cards_per_person)
            self.comps = [self.computer_player1]

    def change_middle_card(self, card: Card) -> None:
        """
        Enables to change the card on the table.

        :param card: a player who wins round lay his card on the middlecard
        :type card: Card
        """
        self.middlecard: Card = card

    def choose_winner(self) -> Computer:
        """
        Chooses winner of a single round between computer players
        if player did not answer right.

        :return: Computer object
        :rtype: Computer
        """
        if self._amount_of_computers == 3:
            winner: Computer = choice(
                [
                    self.computer_player1,
                    self.computer_player2,
                    self.computer_player3,
                ]
            )
        elif self._amount_of_computers == 2:
            winner: Computer = choice(
                [self.computer_player1, self.computer_player2],
            )
        else:
            winner: Computer = self.computer_player1
        return winner

    def verify_if_game_has_ended(self) -> Optional[str]:
        """
        Verifies if the game has ended.

        :return: Winning message if the game has ended, None otherwise
        :rtype: Optional[str]
        """
        if self.player.has_won():
            return "You win."
        for comp in self.comps:
            if comp.has_won():
                return f"{comp.name} wins."

    def player_failed(self, should_print: bool = False) -> Optional[bool]:
        """
        Handles situation if player did not manage to find common symbol.

        :param should_print: describe if method should print or not
        :type should_print: bool
        :return: True if the player failed, None otherwise
        :rtype: Optional[bool]
        """
        winner = self.choose_winner()
        symbol = winner.get_common_symbol(self.middlecard)
        if should_print:
            print(f"{winner.name} has won this round. Common symbol: {symbol}")
        self.change_middle_card(winner.first_card())
        winner.remove_card(winner.first_card())
        if winner.has_won():
            if should_print:
                print(f"{winner.name} winning it all! It runs out of cards.")
            return True

    def play(self) -> None:
        """
        Interface of the game.
        """
        while self.player.cards:
            print(self.middlecard.symbols)
            print(self.player.first_card().symbols)
            self.set_timeout()
            answer = input_with_timeout(
                "Choose the common symbol: ",
                randint(self._timeout - 2, self._timeout + 2),
            )
            if not answer:
                if self.player_failed(should_print=True):
                    break
            else:
                symbol_found, game_won = self.check_symbol(answer)
                if symbol_found:
                    print("You're right")
                    if game_won:
                        print("You win")
                        break
                else:
                    print("Wrong answer")
                    if self.player_failed(should_print=True):
                        break

    def check_symbol(self, symbol: str) -> tuple[bool, bool]:
        """
        Checks if the provided symbol is in the middle card's symbols. If it is, changes the middle card to the player's first card,
        removes the player's first card, and checks if the game has ended.

        :param symbol: The symbol to check.
        :type symbol: str
        :return: A tuple where the first element is True if the symbol was in the middle card's symbols and False otherwise,
                and the second element is True if the game has ended with a win and False otherwise.
        :rtype: Tuple[bool, bool]
        """
        if symbol in self.middlecard.symbols:
            self.change_middle_card(
                self.player.first_card(),
            )
            self.player.remove_card(
                self.player.first_card(),
            )
            win = "You win."
            if self.verify_if_game_has_ended() == win:
                return True, True
            else:
                return True, False
        else:
            return False, False
