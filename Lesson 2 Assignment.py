#!/usr/bin/env python3
#age_calculator.py

first_name=input("What is your first name?\n")
last_name=input("What is your last name?\n")
current_year=input("What is the current year?\n")
birth_year=input("What is your birth year?\n")

age = int(current_year) - int(birth_year)

print("Your age is ~" + str(age) + "!\n")
print(f"Next year you will be ~{age + 1}!\n")

print("--------------------------\nWritten by Peyton Tharp")
