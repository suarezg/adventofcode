import re

# line = "Game 1: 1 green, 6 red, 4 blue; 2 blue, 6 green, 7 red; 3 red, 4 blue, 6 green; 3 green; 3 blue, 2 green, 1 red"

def find_max(line,pattern) -> int:    
    matches = re.findall(pattern, line)
    if not matches:
        return 0

    counts = [int(m) for m in matches]
    return max(counts)

def calc_power_set(line) -> int:
    reds =find_max(line, '([0-9]+) red')
    greens = find_max(line, '([0-9]+) green')
    blues = find_max(line, '([0-9]+) blue')

    return reds * greens * blues 

result = 0
with open('input.txt', 'r') as file:
    for line in file:
        result += calc_power_set(line)

print(result)            


            