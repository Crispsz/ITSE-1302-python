#!/usr/bin/env python3
# grade_calculator.py

import random

grades = []
grade = int

while (True):
    grade = int(input("Please enter your grade or -1 to stop: "))
    if (grade == -1):
        break
    else:
        grades.append(grade)

print(f'{grades}')
print("\nRemoving Lowest Grade")

grades.pop(grades.index(min(grades)))

print(f'{grades}')
print("\nRemoving Random Grade")

grades.remove(random.choice(grades))

print(f'{grades}')
print("Edit a grade")

for i in range(len(grades)):
    print(f'{i+1}. {grades[i]}')

while(True):
    edit = int(input("Which grade do you want to edit: "))
    
    if edit > len(grades) or edit <= 0:
        print(f'Enter a number between 1 and {len(grades)}')
    else:
        grades.pop(edit-1)
        new_grade = int(input("Enter the new grade: "))
        grades.insert(edit-1, new_grade)
        print(f'{grades}')
        break

print("Sorting and reversing list...")
grades.sort(reverse=True)

print(grades)
print("Getting grade total and average")
print(sum(grades))
print(sum(grades)/len(grades))
print("--------------------------------\nCompleted by, Peyton Tharp")
