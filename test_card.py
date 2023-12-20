from card import Card
import pytest
from exceptions import SymbolsError


def test_card_create():
    symbols = [1, 2, 3, 4, 5]
    card = Card(symbols)
    assert card.symbols == symbols


def test_card_set_symbols():
    symbols = [1, 2, 3, 4, 5]
    card = Card(symbols)
    assert card.symbols == symbols
    new_symbols = [2, 3, 4, 5, 6]
    card.symbols = new_symbols
    assert card.symbols == new_symbols


def test_card_set_symbols_invalid_len():
    symbols = [1, 2, 3, 4, 5]
    card = Card(symbols)
    assert card.symbols == symbols
    new_symbols = [2, 3, 4, 5]
    with pytest.raises(SymbolsError):
        card.symbols = new_symbols


def test_shuffle_symbols(monkeypatch):
    monkeypatch.setattr("card.shuffle", lambda card: [card[::-1]])
    card1 = Card(["a", "b", "c", "d"])
    card1.shuffle_symbols()
    card1.symbols = ["d", "c", "b", "a"]
