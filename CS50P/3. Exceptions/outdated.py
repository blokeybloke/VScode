# List of month names
months = ["January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"]

while True:
    user_input = input("Enter a date (e.g., 9/8/1636 or September 8, 1636): ")

    # Split input based on space and slash
    if "/" in user_input:
        parts = user_input.split("/")
        if len(parts) == 3:
            month, day, year = parts
            # Check if they are all digits
            if month.isdigit() and day.isdigit() and year.isdigit():
                # Check if month and day are in valid ranges
                if 1 <= int(month) <= 12 and 1 <= int(day) <= 31:
                    print(f"{year}-{int(month):02d}-{int(day):02d}")
                    break
                else:
                    print("Month or day out of range.")
            else:
                print("Please enter numbers for month, day, and year.")
        else:
            print("Invalid format. Make sure to use MM/DD/YYYY.")
    elif any(month in user_input for month in months):
        parts = user_input.replace(",", "").split()
        if len(parts) == 3 and parts[1].isdigit() and parts[2].isdigit():
            month_name, day, year = parts
            # Check if day is in a valid range
            if 1 <= int(day) <= 31:
                month_number = months.index(month_name) + 1
                print(f"{year}-{month_number:02d}-{int(day):02d}")
                break
            else:
                print("Day out of range.")
        else:
            print("Invalid format. Make sure to use 'Month DD, YYYY'.")
    else:
        print("Invalid format or month name.")
