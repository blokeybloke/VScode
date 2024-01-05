# Define a function to remove vowels from a given string
def omit_vowels(input_string):
    vowels = "aeiouAEIOU"
    result = ""
    # Iterate over each character in the input string
    for letter in input_string:
        # Check if the current character is not a vowel
        if letter not in vowels:
            # If it's not a vowel, append it to the result string
            result += letter

    return result

name = input("Input: ")
# Call the omit_vowels function with the user input and print the result
print("Output:", omit_vowels(name))