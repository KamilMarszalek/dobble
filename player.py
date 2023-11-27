class Player:
    def __init__(self, cards) -> None:
        self.cards = cards

    def first_card(self):
        return self.cards[0]

    def remove_card(self, card):
        self.cards.remove(card)

    # def verify_answer(self, answer):
    #     first_card = self.first_card()
    #     if answer in first_card:
    #         self.cards.remove(first_card)
    #         if self.verify_if_win():
    #             return "Win"
    #         return True
    #     else:
    #         return False

    def verify_if_win(self):
        if not self.cards:
            return True
        return False
