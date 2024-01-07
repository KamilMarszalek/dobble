from card import Card


def test_card_create():
    symbols = ["1", "2", "3", "4", "5"]
    card = Card(symbols)
    assert card.symbols == symbols


def test_shuffle_symbols(monkeypatch):
    def reverse_symbols(self):
        self._symbols.reverse()

    monkeypatch.setattr("card.Card.shuffle_symbols", reverse_symbols)
    card1 = Card(["a", "b", "c", "d"])
    card1.shuffle_symbols()
    assert card1.symbols == ["d", "c", "b", "a"]
