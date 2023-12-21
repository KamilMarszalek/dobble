import random

NUMBERS_IN_POLISH = {
    1: "jeden",
    2: "dwa",
    3: "trzy",
    4: "cztery",
    5: "pięć",
    6: "sześć",
    7: "siedem",
    8: "osiem",
    9: "dziewięć",
    10: "dziesięć",
    11: "jedenaście",
    12: "dwanaście",
    13: "trzynaście",
    14: "czternaście",
    15: "piętnaście",
    16: "szesnaście",
    17: "siedemnaście",
    18: "osiemnaście",
    19: "dziewiętnaście",
    20: "dwadzieścia",
    21: "dwadzieścia jeden",
    22: "dwadzieścia dwa",
    23: "dwadzieścia trzy",
    24: "dwadzieścia cztery",
    25: "dwadzieścia pięć",
    26: "dwadzieścia sześć",
    27: "dwadzieścia siedem",
    28: "dwadzieścia osiem",
    29: "dwadzieścia dziewięć",
    30: "trzydzieści",
    31: "trzydzieści jeden",
    32: "trzydzieści dwa",
    33: "trzydzieści trzy",
    34: "trzydzieści cztery",
    35: "trzydzieści pięć",
    36: "trzydzieści sześć",
    37: "trzydzieści siedem",
    38: "trzydzieści osiem",
    39: "trzydzieści dziewięć",
    40: "czterdzieści",
    41: "czterdzieści jeden",
    42: "czterdzieści dwa",
    43: "czterdzieści trzy",
    44: "czterdzieści cztery",
    45: "czterdzieści pięć",
    46: "czterdzieści sześć",
    47: "czterdzieści siedem",
    48: "czterdzieści osiem",
    49: "czterdzieści dziewięć",
    50: "pięćdziesiąt",
    51: "pięćdziesiąt jeden",
    52: "pięćdziesiąt dwa",
    53: "pięćdziesiąt trzy",
    54: "pięćdziesiąt cztery",
    55: "pięćdziesiąt pięć",
    56: "pięćdziesiąt sześć",
    57: "pięćdziesiąt siedem",
}


def generate_pack(number_of_symbols: int) -> list[list[str]]:
    """Generate a pack of dobble cards."""
    if number_of_symbols < 3 or number_of_symbols > 8:
        raise ValueError("Number of symbols must be between 3 and 8.")
    numbers_of_symbols = number_of_symbols
    pack = []
    n = numbers_of_symbols - 1  # n must be a prime number or a power of prime number
    if n == 6:  # for seven symbols per card standard approach cannot be applied
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


def generate_approximate_dobble_pack(total_symbols, symbols_per_card, max_cards):
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


generate_approximate_dobble_pack(46, 7, 43)
