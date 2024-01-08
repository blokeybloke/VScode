responses = {}
# Set a flag to indicate polling is active
polling_active = True
# Get user name and response
while polling_active:
    name = input("\nWhat is your name? ")
    response = input("What mountain would you like to climb one day? ")
# Store response in dictionary
    responses[name] = response
# Find out if anyone else is going to take the poll
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == "no":
        polling_active = False

# Polling complete, show the results
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")

# Challenge - Dream vacation
vacation = {}

polling = True
while polling:
    dream = input("If you can could anywhere, where would you go? ")

    vacation = dream 
    
    polling = False

print(f"\n{dream} is the best.")