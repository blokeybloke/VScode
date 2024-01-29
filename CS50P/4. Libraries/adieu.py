people = ["liesl", "friedrich", "louisa", "kurt", "brigitta", "marta", "gretl"]

user = input("Name: ")

for peep in people:
    if peep in people:
        print(f"Adieu, adieu, to {people[0].title()}")
        break