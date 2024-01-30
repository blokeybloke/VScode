# List of predefined names
people = ["Liesl", "Friedrich", "Louisa", "Kurt", "Brigitta", "Marta", "Gretl"]
# List to store valid names
valid_names = []
# Start infinite loop
while True:
    try:
        user = input()
    # Break the loop
    except EOFError:
        break
    # Check if user wants to exit loop
    if user.lower() == "exit":
        break
    # Strip leading/trailing spaces and capitalise the first letter
    name = user.strip(). capitalize()
    
    # Check if the capitalized name is in the list, regardless of the case
    if any(name.lower() == person.lower() for person in people):
        valid_names.append(name)
# After loop, check if there are any valid names
if valid_names:
    # Format list of names based on number of names
    if len(valid_names) > 2:
        # Join all names with commas. Use "and" for last name
        rule = ", ".join(valid_names[:-1]) + ", and " + valid_names[-1]
    elif len(valid_names) == 2:
        # If there a only 2 names, use "and"
        rule = " and ".join(valid_names)
    else:
        # If only one name, use as is
        rule = valid_names[0]
    print(f"Adieu, adieu, to {rule}")
