
def extrapolate(numbers) -> int:
    if all(n == 0 for n in numbers):
        return 0
    
    differences = [t - s for s, t in zip(numbers, numbers[1:])]
    addition = extrapolate(differences)
    return differences[-1] + addition

with open('input.txt') as file:
    result = 0
    for line in file:
        numbers = [int(num) for num in line.strip().split()]
        numbers.reverse()
        result += extrapolate(numbers) + numbers[-1]


    print(f"Result: {result}")
