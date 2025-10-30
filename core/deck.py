import random

def build_standard_deck() -> list[dict]:
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    deck = [{'rank': rank, 'suit': suit} for suit in suits for rank in ranks]
    return deck

def shuffle_by_suit(deck: list[dict], swaps: int = 5000) -> list[dict]:
    suit_indices = {}
    for index, card in enumerate(deck):
        suit = card['suit']
        if suit not in suit_indices:
            suit_indices[suit] = []
        suit_indices[suit].append(index)

    for _ in range(swaps):
        suit = random.choice(list(suit_indices.keys()))
        indices = suit_indices[suit]
        if len(indices) < 2:
            continue
        i1, i2 = random.sample(indices, 2)
        deck[i1], deck[i2] = deck[i2], deck[i1]
    return deck



