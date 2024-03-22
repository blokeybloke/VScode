def main():
    while True:
        fraction_input = input("Fraction: ")
        try:
            percentage = convert(fraction_input)
            message = gauge(percentage)
            if message:
                print(message)
                break
        except (ValueError, ZeroDivisionError):
            continue

def convert(fraction):
    numerator, denominator = map(int, fraction.split('/'))
    return round((numerator / denominator) * 100)

def gauge(percentage):
    if percentage == 1 or percentage == 99:
        return "E" if percentage == 1 else "F"
    elif percentage == 0:
        return "E"
    elif percentage == 100:
        return "F"
    elif 0 < percentage < 100:
        return f"{percentage}%"
    # If the percentage is outside 0-100, it implies an invalid or unusual input, so return None
    return None

if __name__ == "__main__":
    main()