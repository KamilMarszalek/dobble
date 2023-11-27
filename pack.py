def generate_pack(x):
    numbers_in_polish = {
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
    if x < 3 or x > 8:
        raise ValueError("Number of symbols must be between 3 and 8.")
    symbols_on_card = x
    pack = []
    n = symbols_on_card - 1
    for i in range(n + 1):
        pack.append([numbers_in_polish[1]])
        for j in range(n):
            pack[i].append(numbers_in_polish[(j + 1) + (i * n) + 1])
    for i in range(0, n):
        for j in range(0, n):
            pack.append([numbers_in_polish[i + 2]])
            for k in range(0, n):
                value = (n + 1 + n * k + (i * k + j) % n) + 1
                pack[len(pack) - 1].append(numbers_in_polish[value])
    return pack