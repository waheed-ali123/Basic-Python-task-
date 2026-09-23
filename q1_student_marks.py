"""
Question No1
Ask the user for the marks of 5 subjects and calculate:
- Total marks
- Percentage
- Grade
- Pass/Fail
"""

def get_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"


def main():
    num_subjects = 5
    marks = []

    for i in range(1, num_subjects + 1):
        while True:
            try:
                mark = float(input(f"Enter marks for subject {i} (out of 100): "))
                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("Please enter a value between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    total = sum(marks)
    percentage = total / num_subjects
    grade = get_grade(percentage)
    result = "Pass" if percentage >= 50 else "Fail"

    print("\n--- Result ---")
    print(f"Total Marks   : {total}/{num_subjects * 100}")
    print(f"Percentage    : {percentage:.2f}%")
    print(f"Grade         : {grade}")
    print(f"Result        : {result}")


if __name__ == "__main__":
    main()
