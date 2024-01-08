# Start with users that need to be verified
# An empty list to hold confirmed
unconfirmed_users = ["alice", "brian", "candace"]
confirmed_users = []
# Verify each user until there are no more unconfirmed
# Move each verified to confimed user list
while unconfirmed_users:
    current_users = unconfirmed_users.pop()

    print(f"Verifying user: {current_users.title()}")
    confirmed_users.append(current_users)

# Display all confirmed users
    print("\nThe following users have been confirmed: ")
    for confirmed_user in confirmed_users:
        print(confirmed_user.title())

# Challenge - Deli & No pastrami
sandwich_orders = ["chicken", "pastrami", "meatball", "veggie", "pastrami"]
finished_sandwiches = []

print("The deli has run out of pastrami.")
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

print(f"This is what we have left {sandwich_orders}.")

while sandwich_orders:
    sandwiches = sandwich_orders.pop()
    print(f"I made your {sandwiches} sandwich.")

    finished_sandwiches.append(sandwiches)

    print(f"\nThe follwing sandwiches have been made: ")
    for finished in finished_sandwiches:
        print(finished)

