def main():
    name = input("Input: ")
    print("Output:", shorten(name))

def shorten(word):
    vowels = "aeiouAEIOU"
    result = ""
    for letter in word:
        if letter not in vowels:
            result += letter
    return result

if __name__ == "__main__":
    main()
