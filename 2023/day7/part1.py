
from enum import Enum
from collections import namedtuple


class HandStrength(Enum):
    HIGH_CARD = 0
    ONE_PAIR = 1
    TWO_PAIR = 2
    THREE_OF_A_KIND = 3
    FULL_HOUSE = 4
    FOUR_OF_A_KIND = 5
    FIVE_OF_A_KIND = 6

    def __lt__(self, other):
        return self.value < other.value

Hand = namedtuple('Hand', ['strength', 'hand', 'bid'])
cards = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']


def classify(hand) -> HandStrength:
    counts = [0] * len(cards)
    counts = [list(hand).count(c) for c in cards]

    if any(count == 5 for count in counts):
        return HandStrength.FIVE_OF_A_KIND
    if any(count == 4 for count in counts):
        return HandStrength.FOUR_OF_A_KIND 
    if any(count == 3 for count in counts) and any(count == 2 for count in counts):
        return HandStrength.FULL_HOUSE
    if any(count == 3 for count in counts):
        return HandStrength.THREE_OF_A_KIND
    if counts.count(2) == 2:
        return HandStrength.TWO_PAIR
    if any(count == 2 for count in counts):
        return HandStrength.ONE_PAIR
    
    return HandStrength.HIGH_CARD

def order(hand):
    t = tuple([cards.index(c) for c in hand])
    return t

with open('input.txt') as file:

    hands = []
    for line in file:
        [hand, bid] = line.split()

        # print(f"hand: {hand}, bid: {bid}, strength: {classify(hand)}, order: {order(hand)}")
        hands.append(Hand(classify(hand), order(hand), int(bid)))
        
    hands.sort()
    result = 0
    for rank, h in enumerate(hands):
        result += h.bid * (rank + 1) 
    print(f"Result: {result}")