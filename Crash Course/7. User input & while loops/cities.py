# Break to exit loop
prompt = "Please enter the name of a city you have visited: "
prompt += "\nEnter 'quit' when you have finished. "

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")