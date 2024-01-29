people = ["Liesl", "Friedrich", "Louisa", "Kurt", "Brigitta", "Marta", "Gretl"]

valid_names = []

while True:
    user = input("Name: ")
    
    if user.lower() == "exit":
        break

    name = user.strip(). capitalize()

    if name in people:
        valid_names.append(name)


if valid_names:
    if len(valid_names) > 1:
        rule = ", ".join(valid_names[:-1]) + " and " + valid_names[-1]
    else:
        rule = valid_names[0]
    print(f"Adieu, adieu, to {rule}")
