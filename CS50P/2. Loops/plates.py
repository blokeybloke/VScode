def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # Check if the length of the string is within the proper range
    def is_proper_length(string):
        return 2 <= len(string) <= 6
    # Check if the first two characters are alphabetic
    def starts_with_two_letters(string):
        return string[:2].isalpha()
    # Check if alphanumeric (contains only letters and numbers)
    def is_alphanumeric(string):
        return string.isalnum()
    # Ensure no digit appears before a letter
    def no_digit_before_letter(string):
        for i in range(len(string) - 1):
            if string[i].isdigit() and string[i+1].isalpha():
                return False
        return True
    # Ensure the first digit is not zero
    def first_digit_not_zero(string):
        for char in string:
            if char.isdigit():
                return char != '0'
        return True

    # Execute all helper functions
    return (is_proper_length(s) and
        starts_with_two_letters(s) and
        is_alphanumeric(s) and
        no_digit_before_letter(s) and
        first_digit_not_zero(s))

main()