print("meow")
print("meow")
print("meow")

# while loop
i = 3
while i !=0:
    print("meow")
    i = i - 1

i = 0
while i < 3:
    print("meow")
    i += 1

# for loop in list
for i in [0, 1, 2]:
    print("meow")

# for loop with range (use _ for unimportant variable)
for _ in range(3):
    print("woof")

print("meow\n" * 3, end="")

# Validating input
while True:
    n = int(input("What's n? "))
    if n > 0:
        break

for _ in range(n):
    print("meow")

# Define meow
def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            break
    return n

def meow(n):
    for _ in range(n):
        print("meow")