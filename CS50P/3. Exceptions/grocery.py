item_counts = {}

# Loop to get user input
while True:
    try:
    # Ask for item input or a command to stop
        item_input = input()
    except EOFError:
        break
    
    # Check if the user wants to finish
    if item_input.lower() == 'done':
        break

    # Convert the item to uppercase
    item = item_input.upper()

    # Increment the count of the item in the dictionary
    if item in item_counts:
        item_counts[item] += 1
    else:
        item_counts[item] = 1

# Print the items and their counts
print()
for item in sorted(item_counts):
    print(f"{item_counts[item]} {item}")