def main():
    user = input("What time is it? ")
    time = convert(user)
    if time >= 7 and time <= 8:
        print("breakfast time")
    if time >= 12 and time <= 13:
        print("lunch time")
    if time >= 18 and time <= 19:
        print("dinner time")


def convert(time):
    hours, minutes = map(int, time.split(":"))
    new_time = hours + minutes / 60
    return new_time

if __name__ == "__main__":
    main()