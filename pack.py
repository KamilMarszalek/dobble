import random
from constants import NUMBERS_IN_POLISH


def generate_pack(number_of_symbols: int) -> list[list[str]]:
    """
    Generate a pack of dobble cards.

    :param number_of_symbols: amount of symbols on a single card
    :type number_of_symbols: int
    :return: a pack of dobble cards
    :rtype: list[list[str]]
    :raises ValueError: if number of symbols is not between 3 and 8
    """
    if number_of_symbols < 3 or number_of_symbols > 8:
        raise ValueError("Number of symbols must be between 3 and 8.")
    numbers_of_symbols = number_of_symbols
    pack = []
    n = numbers_of_symbols - 1  # n must be a power of prime number
    if n == 6:  # for 7 symbols per card standard approach cannot be applied
        return generate_approximate_dobble_pack(43, 7, 43)
    for i in range(n + 1):
        pack.append([NUMBERS_IN_POLISH[1]])
        for j in range(n):
            pack[i].append(NUMBERS_IN_POLISH[(j + 1) + (i * n) + 1])
    for i in range(0, n):
        for j in range(0, n):
            pack.append([NUMBERS_IN_POLISH[i + 2]])
            for k in range(0, n):
                value = (n + 1 + n * k + (i * k + j) % n) + 1
                pack[len(pack) - 1].append(NUMBERS_IN_POLISH[value])
    return pack


def generate_approximate_dobble_pack(
    total_symbols, symbols_per_card, max_cards
) -> list[list[str]]:
    """
    Generate an approximate dobble pack for 7 symbols on a card.

    :param total_symbols: amount of total symbols which can be used
    :type total_symbols: int
    :param symbols_per_card: amount of symbols on a single card
    :type symbols_per_card: int
    :param max_cards: amount of cards to be generated
    :type max_cards: int
    :return: an approximate dobble pack
    :rtype: list[list[str]]
    """
    symbols = list(range(1, total_symbols + 1))
    pack = []
    ready_pack = []

    while len(pack) < max_cards:
        random.shuffle(symbols)
        new_card = symbols[:symbols_per_card]
        if all(any(symbol in card for symbol in new_card) for card in pack):
            pack.append(new_card)
    for card in pack:
        ready_pack.append([NUMBERS_IN_POLISH[symbol] for symbol in card])
    print(pack)
    return ready_pack
