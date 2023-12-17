from game import Game
import pytest
from exceptions import DiffLevelError, InvalidComputersAmount
from card import Card


def test_game_create():
    new_game = Game(3, 3, 8)
    assert new_game.amount_of_computers == 3
    assert new_game.diff_level == 3
    assert new_game.number_of_symbols == 8
    assert new_game._pack == [
        ["jeden", "dwa", "trzy", "cztery", "pięć", "sześć", "siedem", "osiem"],
        [
            "jeden",
            "dziewięć",
            "dziesięć",
            "jedenaście",
            "dwanaście",
            "trzynaście",
            "czternaście",
            "piętnaście",
        ],
        [
            "jeden",
            "szesnaście",
            "siedemnaście",
            "osiemnaście",
            "dziewiętnaście",
            "dwadzieścia",
            "dwadzieścia jeden",
            "dwadzieścia dwa",
        ],
        [
            "jeden",
            "dwadzieścia trzy",
            "dwadzieścia cztery",
            "dwadzieścia pięć",
            "dwadzieścia sześć",
            "dwadzieścia siedem",
            "dwadzieścia osiem",
            "dwadzieścia dziewięć",
        ],
        [
            "jeden",
            "trzydzieści",
            "trzydzieści jeden",
            "trzydzieści dwa",
            "trzydzieści trzy",
            "trzydzieści cztery",
            "trzydzieści pięć",
            "trzydzieści sześć",
        ],
        [
            "jeden",
            "trzydzieści siedem",
            "trzydzieści osiem",
            "trzydzieści dziewięć",
            "czterdzieści",
            "czterdzieści jeden",
            "czterdzieści dwa",
            "czterdzieści trzy",
        ],
        [
            "jeden",
            "czterdzieści cztery",
            "czterdzieści pięć",
            "czterdzieści sześć",
            "czterdzieści siedem",
            "czterdzieści osiem",
            "czterdzieści dziewięć",
            "pięćdziesiąt",
        ],
        [
            "jeden",
            "pięćdziesiąt jeden",
            "pięćdziesiąt dwa",
            "pięćdziesiąt trzy",
            "pięćdziesiąt cztery",
            "pięćdziesiąt pięć",
            "pięćdziesiąt sześć",
            "pięćdziesiąt siedem",
        ],
        [
            "dwa",
            "dziewięć",
            "szesnaście",
            "dwadzieścia trzy",
            "trzydzieści",
            "trzydzieści siedem",
            "czterdzieści cztery",
            "pięćdziesiąt jeden",
        ],
        [
            "dwa",
            "dziesięć",
            "siedemnaście",
            "dwadzieścia cztery",
            "trzydzieści jeden",
            "trzydzieści osiem",
            "czterdzieści pięć",
            "pięćdziesiąt dwa",
        ],
        [
            "dwa",
            "jedenaście",
            "osiemnaście",
            "dwadzieścia pięć",
            "trzydzieści dwa",
            "trzydzieści dziewięć",
            "czterdzieści sześć",
            "pięćdziesiąt trzy",
        ],
        [
            "dwa",
            "dwanaście",
            "dziewiętnaście",
            "dwadzieścia sześć",
            "trzydzieści trzy",
            "czterdzieści",
            "czterdzieści siedem",
            "pięćdziesiąt cztery",
        ],
        [
            "dwa",
            "trzynaście",
            "dwadzieścia",
            "dwadzieścia siedem",
            "trzydzieści cztery",
            "czterdzieści jeden",
            "czterdzieści osiem",
            "pięćdziesiąt pięć",
        ],
        [
            "dwa",
            "czternaście",
            "dwadzieścia jeden",
            "dwadzieścia osiem",
            "trzydzieści pięć",
            "czterdzieści dwa",
            "czterdzieści dziewięć",
            "pięćdziesiąt sześć",
        ],
        [
            "dwa",
            "piętnaście",
            "dwadzieścia dwa",
            "dwadzieścia dziewięć",
            "trzydzieści sześć",
            "czterdzieści trzy",
            "pięćdziesiąt",
            "pięćdziesiąt siedem",
        ],
        [
            "trzy",
            "dziewięć",
            "siedemnaście",
            "dwadzieścia pięć",
            "trzydzieści trzy",
            "czterdzieści jeden",
            "czterdzieści dziewięć",
            "pięćdziesiąt siedem",
        ],
        [
            "trzy",
            "dziesięć",
            "osiemnaście",
            "dwadzieścia sześć",
            "trzydzieści cztery",
            "czterdzieści dwa",
            "pięćdziesiąt",
            "pięćdziesiąt jeden",
        ],
        [
            "trzy",
            "jedenaście",
            "dziewiętnaście",
            "dwadzieścia siedem",
            "trzydzieści pięć",
            "czterdzieści trzy",
            "czterdzieści cztery",
            "pięćdziesiąt dwa",
        ],
        [
            "trzy",
            "dwanaście",
            "dwadzieścia",
            "dwadzieścia osiem",
            "trzydzieści sześć",
            "trzydzieści siedem",
            "czterdzieści pięć",
            "pięćdziesiąt trzy",
        ],
        [
            "trzy",
            "trzynaście",
            "dwadzieścia jeden",
            "dwadzieścia dziewięć",
            "trzydzieści",
            "trzydzieści osiem",
            "czterdzieści sześć",
            "pięćdziesiąt cztery",
        ],
        [
            "trzy",
            "czternaście",
            "dwadzieścia dwa",
            "dwadzieścia trzy",
            "trzydzieści jeden",
            "trzydzieści dziewięć",
            "czterdzieści siedem",
            "pięćdziesiąt pięć",
        ],
        [
            "trzy",
            "piętnaście",
            "szesnaście",
            "dwadzieścia cztery",
            "trzydzieści dwa",
            "czterdzieści",
            "czterdzieści osiem",
            "pięćdziesiąt sześć",
        ],
        [
            "cztery",
            "dziewięć",
            "osiemnaście",
            "dwadzieścia siedem",
            "trzydzieści sześć",
            "trzydzieści osiem",
            "czterdzieści siedem",
            "pięćdziesiąt sześć",
        ],
        [
            "cztery",
            "dziesięć",
            "dziewiętnaście",
            "dwadzieścia osiem",
            "trzydzieści",
            "trzydzieści dziewięć",
            "czterdzieści osiem",
            "pięćdziesiąt siedem",
        ],
        [
            "cztery",
            "jedenaście",
            "dwadzieścia",
            "dwadzieścia dziewięć",
            "trzydzieści jeden",
            "czterdzieści",
            "czterdzieści dziewięć",
            "pięćdziesiąt jeden",
        ],
        [
            "cztery",
            "dwanaście",
            "dwadzieścia jeden",
            "dwadzieścia trzy",
            "trzydzieści dwa",
            "czterdzieści jeden",
            "pięćdziesiąt",
            "pięćdziesiąt dwa",
        ],
        [
            "cztery",
            "trzynaście",
            "dwadzieścia dwa",
            "dwadzieścia cztery",
            "trzydzieści trzy",
            "czterdzieści dwa",
            "czterdzieści cztery",
            "pięćdziesiąt trzy",
        ],
        [
            "cztery",
            "czternaście",
            "szesnaście",
            "dwadzieścia pięć",
            "trzydzieści cztery",
            "czterdzieści trzy",
            "czterdzieści pięć",
            "pięćdziesiąt cztery",
        ],
        [
            "cztery",
            "piętnaście",
            "siedemnaście",
            "dwadzieścia sześć",
            "trzydzieści pięć",
            "trzydzieści siedem",
            "czterdzieści sześć",
            "pięćdziesiąt pięć",
        ],
        [
            "pięć",
            "dziewięć",
            "dziewiętnaście",
            "dwadzieścia dziewięć",
            "trzydzieści dwa",
            "czterdzieści dwa",
            "czterdzieści pięć",
            "pięćdziesiąt pięć",
        ],
        [
            "pięć",
            "dziesięć",
            "dwadzieścia",
            "dwadzieścia trzy",
            "trzydzieści trzy",
            "czterdzieści trzy",
            "czterdzieści sześć",
            "pięćdziesiąt sześć",
        ],
        [
            "pięć",
            "jedenaście",
            "dwadzieścia jeden",
            "dwadzieścia cztery",
            "trzydzieści cztery",
            "trzydzieści siedem",
            "czterdzieści siedem",
            "pięćdziesiąt siedem",
        ],
        [
            "pięć",
            "dwanaście",
            "dwadzieścia dwa",
            "dwadzieścia pięć",
            "trzydzieści pięć",
            "trzydzieści osiem",
            "czterdzieści osiem",
            "pięćdziesiąt jeden",
        ],
        [
            "pięć",
            "trzynaście",
            "szesnaście",
            "dwadzieścia sześć",
            "trzydzieści sześć",
            "trzydzieści dziewięć",
            "czterdzieści dziewięć",
            "pięćdziesiąt dwa",
        ],
        [
            "pięć",
            "czternaście",
            "siedemnaście",
            "dwadzieścia siedem",
            "trzydzieści",
            "czterdzieści",
            "pięćdziesiąt",
            "pięćdziesiąt trzy",
        ],
        [
            "pięć",
            "piętnaście",
            "osiemnaście",
            "dwadzieścia osiem",
            "trzydzieści jeden",
            "czterdzieści jeden",
            "czterdzieści cztery",
            "pięćdziesiąt cztery",
        ],
        [
            "sześć",
            "dziewięć",
            "dwadzieścia",
            "dwadzieścia cztery",
            "trzydzieści pięć",
            "trzydzieści dziewięć",
            "pięćdziesiąt",
            "pięćdziesiąt cztery",
        ],
        [
            "sześć",
            "dziesięć",
            "dwadzieścia jeden",
            "dwadzieścia pięć",
            "trzydzieści sześć",
            "czterdzieści",
            "czterdzieści cztery",
            "pięćdziesiąt pięć",
        ],
        [
            "sześć",
            "jedenaście",
            "dwadzieścia dwa",
            "dwadzieścia sześć",
            "trzydzieści",
            "czterdzieści jeden",
            "czterdzieści pięć",
            "pięćdziesiąt sześć",
        ],
        [
            "sześć",
            "dwanaście",
            "szesnaście",
            "dwadzieścia siedem",
            "trzydzieści jeden",
            "czterdzieści dwa",
            "czterdzieści sześć",
            "pięćdziesiąt siedem",
        ],
        [
            "sześć",
            "trzynaście",
            "siedemnaście",
            "dwadzieścia osiem",
            "trzydzieści dwa",
            "czterdzieści trzy",
            "czterdzieści siedem",
            "pięćdziesiąt jeden",
        ],
        [
            "sześć",
            "czternaście",
            "osiemnaście",
            "dwadzieścia dziewięć",
            "trzydzieści trzy",
            "trzydzieści siedem",
            "czterdzieści osiem",
            "pięćdziesiąt dwa",
        ],
        [
            "sześć",
            "piętnaście",
            "dziewiętnaście",
            "dwadzieścia trzy",
            "trzydzieści cztery",
            "trzydzieści osiem",
            "czterdzieści dziewięć",
            "pięćdziesiąt trzy",
        ],
        [
            "siedem",
            "dziewięć",
            "dwadzieścia jeden",
            "dwadzieścia sześć",
            "trzydzieści jeden",
            "czterdzieści trzy",
            "czterdzieści osiem",
            "pięćdziesiąt trzy",
        ],
        [
            "siedem",
            "dziesięć",
            "dwadzieścia dwa",
            "dwadzieścia siedem",
            "trzydzieści dwa",
            "trzydzieści siedem",
            "czterdzieści dziewięć",
            "pięćdziesiąt cztery",
        ],
        [
            "siedem",
            "jedenaście",
            "szesnaście",
            "dwadzieścia osiem",
            "trzydzieści trzy",
            "trzydzieści osiem",
            "pięćdziesiąt",
            "pięćdziesiąt pięć",
        ],
        [
            "siedem",
            "dwanaście",
            "siedemnaście",
            "dwadzieścia dziewięć",
            "trzydzieści cztery",
            "trzydzieści dziewięć",
            "czterdzieści cztery",
            "pięćdziesiąt sześć",
        ],
        [
            "siedem",
            "trzynaście",
            "osiemnaście",
            "dwadzieścia trzy",
            "trzydzieści pięć",
            "czterdzieści",
            "czterdzieści pięć",
            "pięćdziesiąt siedem",
        ],
        [
            "siedem",
            "czternaście",
            "dziewiętnaście",
            "dwadzieścia cztery",
            "trzydzieści sześć",
            "czterdzieści jeden",
            "czterdzieści sześć",
            "pięćdziesiąt jeden",
        ],
        [
            "siedem",
            "piętnaście",
            "dwadzieścia",
            "dwadzieścia pięć",
            "trzydzieści",
            "czterdzieści dwa",
            "czterdzieści siedem",
            "pięćdziesiąt dwa",
        ],
        [
            "osiem",
            "dziewięć",
            "dwadzieścia dwa",
            "dwadzieścia osiem",
            "trzydzieści cztery",
            "czterdzieści",
            "czterdzieści sześć",
            "pięćdziesiąt dwa",
        ],
        [
            "osiem",
            "dziesięć",
            "szesnaście",
            "dwadzieścia dziewięć",
            "trzydzieści pięć",
            "czterdzieści jeden",
            "czterdzieści siedem",
            "pięćdziesiąt trzy",
        ],
        [
            "osiem",
            "jedenaście",
            "siedemnaście",
            "dwadzieścia trzy",
            "trzydzieści sześć",
            "czterdzieści dwa",
            "czterdzieści osiem",
            "pięćdziesiąt cztery",
        ],
        [
            "osiem",
            "dwanaście",
            "osiemnaście",
            "dwadzieścia cztery",
            "trzydzieści",
            "czterdzieści trzy",
            "czterdzieści dziewięć",
            "pięćdziesiąt pięć",
        ],
        [
            "osiem",
            "trzynaście",
            "dziewiętnaście",
            "dwadzieścia pięć",
            "trzydzieści jeden",
            "trzydzieści siedem",
            "pięćdziesiąt",
            "pięćdziesiąt sześć",
        ],
        [
            "osiem",
            "czternaście",
            "dwadzieścia",
            "dwadzieścia sześć",
            "trzydzieści dwa",
            "trzydzieści osiem",
            "czterdzieści cztery",
            "pięćdziesiąt siedem",
        ],
        [
            "osiem",
            "piętnaście",
            "dwadzieścia jeden",
            "dwadzieścia siedem",
            "trzydzieści trzy",
            "trzydzieści dziewięć",
            "czterdzieści pięć",
            "pięćdziesiąt jeden",
        ],
    ]


def test_game_create_invalid_amount_of_computers():
    with pytest.raises(InvalidComputersAmount):
        Game(4, 3, 3)


def test_game_create_not_existing_diff_level():
    with pytest.raises(DiffLevelError):
        Game(3, 4, 8)


def test_game_set_timeout():
    game1 = Game(3, 3, 8)
    game1.set_timeout()
    assert game1._timeout == 5
    game2 = Game(3, 2, 8)
    game2.set_timeout()
    assert game2._timeout == 15
    game3 = Game(3, 1, 8)
    game3.set_timeout()
    assert game3._timeout == 25


def test_game_create_cards():
    game1 = Game(3, 3, 8)
    game1.create_cards()
    assert len(game1._cards) == 57
    for i in range(len(game1._cards) - 1):
        common_symbols = set(game1._cards[i].symbols).intersection(
            set(game1._cards[i + 1].symbols)
        )
        assert len(common_symbols) == 1


def test_game_deal():
    game1 = Game(3, 3, 8)
    game1.create_cards()
    assert len(game1._cards) == 57
    game1.deal()
    assert len(game1._cards) == 0
    assert len(game1.comp1.cards) == 14
    assert len(game1.comp2.cards) == 14
    assert len(game1.comp3.cards) == 14
    assert len(game1.player.cards) == 14
    assert game1.comp1.cards != game1.comp2.cards
    assert game1.comp1.cards != game1.comp3.cards
    assert game1.comp1.cards != game1.player.cards
    assert game1.comp2.cards != game1.comp1.cards
    assert game1.comp2.cards != game1.comp3.cards
    assert game1.comp2.cards != game1.player.cards
    assert game1.comp3.cards != game1.comp1.cards
    assert game1.comp3.cards != game1.comp2.cards
    assert game1.comp3.cards != game1.player.cards
    game1 = Game(2, 3, 6)
    game1.create_cards()
    assert len(game1._cards) == 31
    game1.deal()
    assert len(game1._cards) == 0
    assert len(game1.comp1.cards) == 10
    assert len(game1.comp2.cards) == 10
    assert len(game1.player.cards) == 10
    assert game1.comp1.cards != game1.comp2.cards
    assert game1.comp1.cards != game1.player.cards
    assert game1.comp2.cards != game1.player.cards

    game1 = Game(1, 3, 3)
    game1.create_cards()
    assert len(game1._cards) == 7
    game1.deal()
    assert len(game1._cards) == 0
    assert len(game1.comp1.cards) == 3
    assert len(game1.player.cards) == 3
    assert game1.comp1.cards != game1.player.cards


def test_game_change_middle_card():
    card = Card(["a", "b", "c"])
    game = Game(3, 3, 8)
    game.create_cards()
    game.deal()
    game.change_middle_card(card)
    assert game._middlecard == card


def test_game_choose_winner(monkeypatch):
    game = Game(3, 3, 8)
    game.create_cards()
    game.deal()
    monkeypatch.setattr("game.choice", lambda x: x[1])
    assert game.choose_winner() == game.comp2
    monkeypatch.setattr("game.choice", lambda x: x[2])
    assert game.choose_winner() == game.comp3
    monkeypatch.setattr("game.choice", lambda x: x[0])
    assert game.choose_winner() == game.comp1
