ASCII_ZERO, ASCII_NINE = ord('0'), ord('9')

digit_texts = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

# total = 0
# with open('input.txt', 'r') as file:
#     for line in file:
#         line = line.strip("\n")

#         l, r = len(line), -1
#         lnum, rnum = "", ""
#         for idx, digit in enumerate(digit_texts):
#             firstTextIndex, lastTextIndex = line.find(digit), line.rfind(digit)
#             firstNumIndex, lastNumIndex = line.find(str(idx)), line.rfind(str(idx))

#             if firstTextIndex != -1 and firstTextIndex < l: 
#                 l = firstTextIndex
#                 lnum = str(idx)

#             if firstNumIndex != -1 and firstNumIndex < l: 
#                 l = firstNumIndex
#                 lnum = str(idx)

#             if lastTextIndex != -1 and lastTextIndex > r: 
#                 r = lastTextIndex
#                 rnum = str(idx)

#             if lastNumIndex != -1 and lastNumIndex > r: 
#                 r = lastNumIndex
#                 rnum = str(idx)

#         print(f"found left: {lnum} at index {l} and right: {rnum} at index {r} for line {line}")
#         total += int(lnum + rnum)

total = 0
with open('input.txt', 'r') as file:
    for line in file:
        line = line.strip("\n")

        l, r = len(line), -1
        lnum, rnum = "", ""
        for idx, digit in enumerate(digit_texts):
            
            for idx, c in enumerate(line):
                if ASCII_ZERO <= ord(c) <= ASCII_NINE:
                    if idx < l:
                        l = idx
                        lnum  = c
                    
                    if idx > r:
                        r = idx
                        rnum = c

            for idx, digit in enumerate(digit_texts):
                first, last = line.find(digit), line.rfind(digit)
                if first != -1 and first < l:
                    l = first
                    lnum = str(idx)

                if last != -1 and last > r:
                    r = last
                    rnum = str(idx)

        print(f"found left: {lnum} at index {l} and right: {rnum} at index {r} for line {line}")
        total += int(lnum + rnum)


print(total)
    


