result = 0
with open('input.txt') as file:
    for line in file:
        _, game = line.strip("\n").split(':')
        [winning, have] = game.split('|')
        wset = set(winning.strip().split())
        have = set(have.strip().split())
        matches = 0
        for num in have:
            if num in wset:
                matches += 1
        result += 2 ** (matches - 1) if matches > 0 else 0

print(f"Result: {result}")