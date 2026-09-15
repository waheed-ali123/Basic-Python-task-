# Question No2
# Advanced Student Marksheet Generator
#
# Author      : Waheed Ali
# Roll No     : 96
# Course      : Internet of Things (IoT)
#
# Takes student's name, roll number, and marks for 5 subjects.
# Calculates total, percentage, grade, and pass/fail result.

def get_grade(percentage):
    if percentage >= 80:
        return "A+"
    elif percentage >= 70:
        return "A"
    elif percentage >= 60:
        return "B"
    elif percentage >= 50:
        return "C"
    elif percentage >= 40:
        return "D"
    else:
        return "F"


def main():
    print("----- Advanced Student Marksheet -----")

    name = input("Enter student's name: ")
    roll_no = input("Enter roll number: ")

    subjects = []
    marks = []

    for i in range(1, 6):
        subject_name = input(f"Enter name of Subject {i}: ")
        while True:
            try:
                subject_marks = float(input(f"Enter marks for {subject_name} (out of 100): "))
                if subject_marks < 0 or subject_marks > 100:
                    print("Marks must be between 0 and 100.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a number.")

        subjects.append(subject_name)
        marks.append(subject_marks)

    total_marks = sum(marks)
    percentage = (total_marks / (len(marks) * 100)) * 100
    grade = get_grade(percentage)

    # Check if student failed in any single subject (below 40)
    failed_any_subject = any(m < 40 for m in marks)

    if failed_any_subject or percentage < 40:
        result = "Fail"
    else:
        result = "Pass"

    # Display complete marksheet
    print("\n===================================")
    print("           STUDENT MARKSHEET        ")
    print("===================================")
    print(f"Name        : {name}")
    print(f"Roll No     : {roll_no}")
    print("-----------------------------------")
    print(f"{'Subject':<20}{'Marks':<10}")
    print("-----------------------------------")
    for subj, mark in zip(subjects, marks):
        print(f"{subj:<20}{mark:<10}")
    print("-----------------------------------")
    print(f"Total Marks : {total_marks:.2f} / {len(marks) * 100}")
    print(f"Percentage  : {percentage:.2f}%")
    print(f"Grade       : {grade}")
    print(f"Result      : {result}")
    print("===================================")


if __name__ == "__main__":
    main()
