# User input
camelCase = input("camelCase: ")

# Print snake_case
print("snake_case: ", end="")

# for loop
for letter in camelCase:
    # Check for uppercase letter
    if letter.isupper():
        # Print underscore and letter in lowercase
        print("_" + letter.lower(), end="")

    else:
        print(letter, end="")

# chatpgt version uses less print
camelCase = input("camelCase: ")

snake_case = ""

for letter in camelCase:
    if letter.isupper():
        snake_case += '_' + letter.lower()
    else:
        snake_case += letter

print("snake_case:", snake_case)