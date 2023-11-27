class Computer:
    def __init__(self, cards, name) -> None:
        self.name = name
        self.cards = cards
        self.score = 0

    def first_card(self):
        return self.cards[0]

    def remove_card(self, card):
        self.cards.remove(card)

    def verify_if_win(self):
        if not self.cards:
            return True
        return False

    def common_symbol(self, card):
        first_card = self.first_card()
        for symbol in first_card.symbols():
            if symbol in card.symbols():
                return symbol
