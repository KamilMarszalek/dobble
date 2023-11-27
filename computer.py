class Computer:
    def __init__(self, cards) -> None:
        self.cards = cards
        self.score = 0

    def first_card(self):
        return self.cards[0]

    def computer_wins_round(self):
        card = self.first_card()
        self.cards.remove(card)
        self.score += 1
        if self.check():
            return True

    def check(self):
        if not self.cards:
            return True
        return False
