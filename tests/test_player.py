from player import Player
from card import Card


def test_player_create():
    card1 = Card(["a", "b", "c"])
    card2 = Card(["a", "d", "e"])
    player = Player([card1, card2])
    assert player.cards == [card1, card2]
    assert player.first_card().symbols == ["a", "b", "c"]


def test_player_remove_card():
    card1 = Card(["a", "b", "c"])
    card2 = Card(["a", "d", "e"])
    player = Player([card1, card2])
    assert player.cards == [card1, card2]
    player.remove_card(card1)
    player.cards == [card2]
    player.remove_card(card2)
    assert player.cards == []


def test_player_has_won():
    card1 = Card(["a", "b", "c"])
    card2 = Card(["a", "d", "e"])
    player = Player([card1, card2])
    assert player.cards == [card1, card2]
    assert player.has_won() is False
    player.remove_card(card1)
    assert player.has_won() is False
    player.remove_card(card2)
    assert player.has_won() is True
