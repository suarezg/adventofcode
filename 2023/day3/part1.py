import re

def sum_part_numbers(matches, symbol_indices) -> int:
    sum = 0
    for number, (start, end) in matches:
        for index in symbol_indices:
            if (start -1) <= index <= end:
                print(f"{number} is a part number")
                sum += int(number)
                break

    return sum

        
result = 0        
with open('input.txt', 'r') as file:

    prev = None
    curr = file.readline().strip('\n')
    while curr:
        next = file.readline().strip('\n')

        matches = [(m.group(), (m.start(), m.end())) for m in re.finditer('[0-9]+', curr)]
        symbol_indices = []
        if prev:
            symbol_indices = [m.start() for m in re.finditer('[^0-9.]', prev)]
            
        symbol_indices = symbol_indices + [m.start() for m in re.finditer('[^0-9.]', curr)]

        if next:
            symbol_indices = symbol_indices + [m.start() for m in re.finditer('[^0-9.]', next)]
            
        line_sum = sum_part_numbers(matches, symbol_indices)
        print(f"linesum: {line_sum}")
        result += line_sum

        prev = curr
        curr = next

print(f"Result: {result}")