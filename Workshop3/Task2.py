i = 0
numbers = []
while i < 5:
    rawNumber = int(input("Enter a Number: "))
    squaredNumber = rawNumber**2
    numbers.append(squaredNumber)
    i += 1

print(numbers)
