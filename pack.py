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

    if not 3 <= number_of_symbols <= 8:
        raise ValueError("Number of symbols must be between 3 and 8.")

    # base_number is used for calculations to generate the correct sequences of symbols

    base_number = (
        number_of_symbols - 1
    )  # base_number must be a power of prime number

    # Handle the special case where the standard generation method doesn't apply

    if base_number == 6:
        return generate_approximate_dobble_pack(43, 7, 43)

    pack = []

    # Generate the first set of cards
    for card_index in range(base_number + 1):
        # Each card starts with the first symbol
        card = [NUMBERS_IN_POLISH[1]]
        # Add subsequent symbols based on the current card index
        for row_index in range(base_number):
            symbol_index = (row_index + 1) + (card_index * base_number) + 1
            card.append(NUMBERS_IN_POLISH[symbol_index])
        pack.append(card)

    # Generate the remaining sets of cards
    for row_index in range(base_number):
        for column_index in range(base_number):
            # Each card starts with a new symbol based on the row_index
            card = [NUMBERS_IN_POLISH[row_index + 2]]
            # Add subsequent symbols based on a calculated value
            for value_index in range(base_number):
                # Calculate the value for the current position
                calc_value = (
                    base_number
                    + 1
                    + base_number * value_index
                    + (row_index * value_index + column_index) % base_number
                ) + 1
                card.append(NUMBERS_IN_POLISH[calc_value])
            pack.append(card)

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
