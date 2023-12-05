
def count_matches(winning, have) -> int:
    matches = 0
    wset = set(winning.strip().split())
    have = set(have.strip().split())
    matches = 0
    for num in have:
        if num in wset:
            matches += 1

    return matches

with open('input.txt') as file:
    lines = file.readlines()
    cards = [1] * len(lines)

    for idx, line in enumerate(lines):
        _, game = line.strip("\n").split(':')
        [winning, have] = game.split('|')
        matches = count_matches(winning,have)
        for i in range(idx + 1, idx + 1 + matches):
            cards[i] += cards[idx]

    print(f"Result: {sum(cards)}")
        
