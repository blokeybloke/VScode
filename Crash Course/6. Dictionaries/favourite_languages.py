favourite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "python"
    }

language = favourite_languages["sarah"].title()
print(f"Sarah's favourite language is {language}.")

# Challenge - Person
vien = {"first": "vien", "last": "diep", "age": 35, "city": "cabramatta"}
print(vien["first"])
print(vien["last"])
print(vien["age"])
print(vien["city"])

# Favourite numbers
favourite_numbers = {
    "vien": "69",
    "fiona": "8",
    "kora": "1"
    }

numbers = favourite_numbers["fiona"].title()
print(f"Fiona's favourite number in {numbers}.")

numbers = favourite_numbers["vien"].title()
print(f"Vien's favourite number in {numbers}.")

numbers = favourite_numbers["kora"].title()
print(f"Kora's favourite number in {numbers}.")

# Glossary
python = {"dictionary": "keys and value",
          "function": "get python to do",
          "list": "store sets of information"
          }
word = python["dictionary"]
print(f"In python, dictionaries hold {word}.")
word_1 = python["function"]
print(f"In python, functions {word_1}s something.")

# for loop
favourite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "python"
    }
for name, language in favourite_languages.items():
    print(f"{name.title()}'s favourite language is {language.title()}.")

# loop through keys or values
favourite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "python"
    }
for language in favourite_languages.keys():
    print(language.title())

# for loop to print msg that match names
favourite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "python"
    }

friends = ["phil", "sarah"]
for name in favourite_languages.keys():
    print(f"Hi {name.title()}.")

    if name in friends:
        language = favourite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language.title()}!")

    if "erin" not in favourite_languages:
        print("Erin, please take the poll!")

# loop using sorted
for name in sorted(favourite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll!")

# Using set to show unique values
favourite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "python"
    }
for language in set(favourite_languages.values()):
    print(language.title())

# Challenge - glossary 2
python = {"dictionary": "keys and value",
          "function": "get python to do",
          "list": "store sets of information"
          }

for terms, description in python.items():
    print(f"I learnt that {terms} means {description}.")

# Rivers
rivers = {"nile" : "egypt",
          "danube" : "russia",
          "thames": "england"
          }

for river, country in rivers.items():
    print(f"The {river.title()} is in {country.title()}.")

for river in rivers.keys():
    print(river.title())

for country in rivers.values():
    print(country.title())

# Polling
favourite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "python"
    }

people = "jen", "sarah", "vien", "fiona"
for person in people:
    if person in favourite_languages:
        print(f"{person.title()}, thank you for taking the poll!")

    if person not in favourite_languages:
        print(f"{person.title()}, please take the poll now!")
