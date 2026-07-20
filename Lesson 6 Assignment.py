#!/usr/bin/env python3
# student_information.py

def main():
    student_info = {
        "Jim": {
            "id": 1,
            "gpa": 3.1,
            "credits-completed": 97.0,
            "grades": [80, 50, 100, 98]
        },
        "Sarah": {
            "id": 2,
            "gpa": 3.6,
            "credits-completed": 40.0,
            "grades": [80, 98]
        }
    }

    print(f"{student_info}\n")

    print("List of Students")
    for i in student_info:
        print(i)

    print("\nStudent Information")
    print("Student\tID\tGPA\tCredits Completed\tGrades")
    for i, j in student_info.items():
        print(f"{i}\t{j['id']}\t{j['gpa']}\t{j['credits-completed']}\t\t\t{j['grades']}")

    print("\nAccessing Student Information Using the Key in a Loop")
    for i in student_info:
        print(f"{i} {student_info[i]}")

    print("\nSarah has dropped out, removing from student info registry")
    student_info.pop("Sarah")
    print(student_info)

    print("\nGetting Jim's GPA")
    print(student_info["Jim"]["gpa"])

    print("\nStudents have graduated, clearing the student registry")
    student_info.clear()
    print(student_info)

    print("--------------------------------\nCompleted by, Peyton Tharp")

if __name__ == '__main__':
    main()
