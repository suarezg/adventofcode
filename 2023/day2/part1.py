import re

MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14

# line = "Game 1: 1 green, 6 red, 4 blue; 2 blue, 6 green, 7 red; 3 red, 4 blue, 6 green; 3 green; 3 blue, 2 green, 1 red"

# matches = re.findall('([0-9]+) red', line)

def validate(line, pattern, limit) -> bool:
    matches = re.findall(pattern, line)
    print(f"matches: {matches} for pattern {pattern}")
    for m in matches:
        if int(m) > limit:
            return False

    return True

def get_game_number(line) -> int:
    match = re.findall('Game ([0-9]+)', line)
    if len(match) != 1:
        print(f"Cannot parse game number on line: {line}")
        assert(False)

    return int(match[0])

# print(f"valid red? {validate(line, '([0-9]+) red', MAX_RED)}")
# print(f"valid green? {validate(line, '([0-9]+) green', MAX_GREEN)}")
# print(f"valid blue? {validate(line, '([0-9]+) blue', MAX_BLUE)}")

result = 0
with open('input.txt', 'r') as file:
    for line in file:
        valid_red = validate(line, '([0-9]+) red', MAX_RED)
        valid_green = validate(line, '([0-9]+) green', MAX_GREEN)
        valid_blue = validate(line, '([0-9]+) blue', MAX_BLUE)

        if valid_red and valid_green and valid_blue:
            result += get_game_number(line)

print(result)            


            