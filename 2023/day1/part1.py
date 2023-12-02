ASCII_ZERO, ASCII_NINE = ord('0'), ord('9')

total = 0
with open('input.txt', 'r') as file:
    for line in file:
        line = line.strip("\n")
        l, r = 0, len(line) - 1
        
        foundL, foundR = False, False

        while (l < r):
            if foundL and foundR: break

            if ~foundL and ASCII_ZERO <= ord(line[l]) <= ASCII_NINE: foundL = True
            else: l += 1

            if ~foundR and ASCII_ZERO <= ord(line[r]) <= ASCII_NINE: foundR = True
            else: r -= 1 
        
        total += int(line[l] + line[r])
        
print(total)
    


