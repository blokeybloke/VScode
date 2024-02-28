def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    def is_proper_length(string):
        return 2 <= len(string) <= 6

    def starts_with_two_letters(string):
        return string[:2].isalpha()

    def is_alphanumeric(string):
        return string.isalnum()

    def no_digit_before_letter(string):
        for i in range(len(string) - 1):
            if string[i].isdigit() and string[i+1].isalpha():
                return False
        return True

    def first_digit_not_zero(string):
        for char in string:
            if char.isdigit():
                return char != '0'
        return True

    return (is_proper_length(s) and
            starts_with_two_letters(s) and
            is_alphanumeric(s) and
            no_digit_before_letter(s) and
            first_digit_not_zero(s))

if __name__ == "__main__":
    main()
