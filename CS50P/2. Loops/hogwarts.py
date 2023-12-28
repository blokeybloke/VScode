students = ["Hermoine", "Harry", "Ron"]

print(students[0])
print(students[1])
print(students[2])

# Use a for loop
for student in students:
    print(student)

# len
for i in range(len(students)):
    print(i + 1, students[i])

# dict
students = {
    "Hermoine": "Gryffindor", 
    "Harry": "Gryffindor", 
    "Ron": "Gryffindor", 
    "Draco": "Slytherin",
    }

for student in students:
    print(student, students[student], sep=", ")

# list of dicts
students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindpr", "patronus": "Jack Russel Terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None}
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")