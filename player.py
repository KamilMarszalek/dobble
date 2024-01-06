from card import Card


class Player:
    """
    Class Player represents a user.

    :param cards: player's cards
    :type cards: list[Card]
    """

    def __init__(self, cards: list[Card], name: str = "You") -> None:
        """
        Initialize the Player class.

        :param cards: player's cards
        :type cards: list[Card]
        """
        self.cards: list[Card] = cards
        self._name: str = name

    @property
    def name(self):
        """
        Returns the name of the player.

        :return: name of the player
        :rtype: str
        """
        return self._name

    def first_card(self) -> Card:
        """
        Returns the first card from the player's cards.

        :return: the first card
        :rtype: Card
        """
        if self.cards:
            return self.cards[0]

    def remove_card(self, card: Card) -> None:
        """
        Removes a card from the player's cards.

        :param card: card to be removed
        :type card: Card
        """
        self.cards.remove(card)

    def has_won(self) -> bool:
        """
        Checks if the player has won.

        :return: True if no cards left, otherwise False
        :rtype: bool
        """
        return not self.cards
