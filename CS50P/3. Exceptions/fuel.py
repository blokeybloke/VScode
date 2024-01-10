# Get user input
while True:
    fraction_input = input("Fraction: ")
    try:
    # Split the input string into numerator and denominator
        numerator, denominator = map(int, fraction_input.split('/'))
    
    # Calculate the percentage
        percentage = round((numerator / denominator) * 100)
        
    # Display the result
        if percentage > 100:
            continue

        elif percentage == 0:
            print("E")
            break

        elif percentage == 100:
            print("F")
            break
        
        elif percentage == 1:
            print("E")
            break
        elif percentage == 99:
            print("F")
            break
        else:
            print(f"{percentage}%")
            break

    except (ValueError, ZeroDivisionError):
        continue
    