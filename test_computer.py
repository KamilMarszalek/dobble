from computer import Computer
from card import Card
import pytest
from exceptions import EmptyNameError


def test_computer_create():
    card1 = Card(["a", "b", "c"])
    card2 = Card(["a", "d", "e"])
    comp = Computer([card1, card2], "comp")
    assert comp.name == "comp"
    assert comp.cards == [card1, card2]


def test_computer_create_empty_name():
    card1 = Card(["a", "b", "c"])
    card2 = Card(["a", "d", "e"])
    with pytest.raises(EmptyNameError):
        Computer([card1, card2], "")


def test_computer_common_symbol():
    card1 = Card(["a", "b", "c"])
    card2 = Card(["a", "d", "e"])
    card3 = Card(["b", "f", "g"])
    mid_card = Card(["c", "d", "f"])
    comp = Computer([card1, card2, card3], "comp")
    assert comp.common_symbol(mid_card) == "c"
    comp.remove_card(comp.first_card())
    assert comp.cards == [card2, card3]
    assert comp.common_symbol(mid_card) == "d"
    comp.remove_card(comp.first_card())
    assert comp.cards == [card3]
    assert comp.common_symbol(mid_card) == "f"
