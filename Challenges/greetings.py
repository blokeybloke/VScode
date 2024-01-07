# 7/01/2024
user = input("What is your name? ")
user_1 = int (input("How old are you? "))

age = 2024 - user_1

print(f"Hello, {user}! Based on your age, you were born in {age}.")

# ChatGPT4
import datetime

user = input("What is your name? ")
user_age = int(input("How old are you? "))

current_year = datetime.datetime.now().year
birth_year = current_year - user_age

print(f"Hello, {user}! Based on your age, you were born in {birth_year}.")
