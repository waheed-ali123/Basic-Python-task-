# Question No1
# Payroll Calculator
# Asks the user for hours worked and hourly rate, then calculates total pay.
# Rule:
#   - If hours <= 40 -> pay = hours * rate
#   - If hours > 40  -> first 40 hours at normal rate,
#                       remaining hours at 1.5 times the hourly rate

def calculate_pay(hours, rate):
    if hours <= 40:
        total_pay = hours * rate
    else:
        overtime_hours = hours - 40
        total_pay = (40 * rate) + (overtime_hours * rate * 1.5)
    return total_pay


def main():
    print("----- Employee Pay Calculator -----")

    try:
        hours = float(input("Enter the number of hours worked: "))
        rate = float(input("Enter the hourly rate: "))
    except ValueError:
        print("Invalid input. Please enter numeric values only.")
        return

    if hours < 0 or rate < 0:
        print("Hours and rate cannot be negative.")
        return

    total_pay = calculate_pay(hours, rate)

    print("\n----- Pay Summary -----")
    print(f"Hours Worked : {hours}")
    print(f"Hourly Rate  : {rate}")
    print(f"Total Pay    : {total_pay:.2f}")


if __name__ == "__main__":
    main()
