months = {
    "January": "1",
    "February": "2",
    "March": "3",
    "April": "4",
    "May": "5",
    "June": "6",
    "July": "7",
    "August": "8",
    "September": "9",
    "October": "10",
    "November": "11",
    "December": "12"
}

def main():

    while True:
        try:
            date = input("Date: ").strip()
            if date[0].isdigit():
                x, y, z = date.split("/")
                x = int(x)
                y = int(y)
                z = int(z)
                if x <= 12 and y <= 31:
                    print(f"{z}-{x:02}-{y:02}")
                    break

            else:
                if "," not in date:
                    print("Invalid date format. Please try again.")
                    continue

                x, y, z = date.split(" ")
                if x in months:
                    x = months[x]
                    y = y.replace(",", "")
                    x = int(x)
                    y = int(y)
                    if x <= 12 and y <= 31:
                        print(f"{z}-{x:02}-{y:02}")
                        break
                    else:
                        print("Invalid date. Please try again.")
                        continue
                else:
                    print("Invalid month name. Please try again.")
                    continue

        except ValueError:
            print("Invalid date format. Please try again.")

main()

