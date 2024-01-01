# Version 1
squares = []
for value in range (1, 11):
    square = value ** 2
    squares.append(square)

print(squares)

# Version 2
squares = []
for value in range (1, 11):
    squares.append(value**2)

print(squares)

# List comprehensions - for loop + new elements + append
squares = [value**2 for value in range(1, 11)]
print(squares)

# Challenge - counting to 20
numbers = list(range(1, 21))
print(numbers)

# Challenge - one in a million
#for value in range(1, 1000000):
#    print(value)

# Challenge - summing a million
numbers = range(1, 1000000)
minimum = min(numbers)
print(minimum)

numbers = range(1, 1000001)
maximum = max(numbers)
print(maximum)

numbers = range(1, 1000001)
result = sum(numbers)
print(result)

# Challenge - Threes
for number in range(3, 31, 3):
    print(number)