import re

def sum_gear_ratios(gear_indices, numbers) -> int:
    sum = 0
    for index in gear_indices:
        adjacent_numbers = []
        for number, (start, end) in numbers:
            if (start -1) <= index <= end:
                adjacent_numbers.append(int(number))

        print(f"adjacent numbers: {adjacent_numbers} for gear at {index}")

        if len(adjacent_numbers) == 2:
            print(f'gear ratio: {adjacent_numbers[0]} x {adjacent_numbers[1]}')
            sum += adjacent_numbers[0] * adjacent_numbers[1]

    return sum
        
result = 0        
with open('input.txt', 'r') as file:

    prev = None
    curr = file.readline().strip('\n')
    while curr:
        next = file.readline().strip('\n')

        gear_indices = [m.start() for m in re.finditer('\*', curr)]
        numbers = []
        if prev:
            numbers = [(m.group(), (m.start(), m.end())) for m in re.finditer('[0-9]+', prev)]
            
        numbers = numbers + [(m.group(), (m.start(), m.end())) for m in re.finditer('[0-9]+', curr)]

        if next:
            numbers = numbers + [(m.group(), (m.start(), m.end())) for m in re.finditer('[0-9]+', next)]
        
        line_sum = sum_gear_ratios(gear_indices, numbers)
        result += line_sum

        prev = curr
        curr = next

print(f"Result: {result}")