"""
Question No3
Ask the user to enter 10 numbers and calculate:
- Sum
- Average
- Largest number
- Smallest number
- Number of even numbers
- Number of odd numbers
"""

def main():
    count = 10
    numbers = []

    for i in range(1, count + 1):
        while True:
            try:
                num = float(input(f"Enter number {i}: "))
                numbers.append(num)
                break
            except ValueError:
                print("Invalid input. Please enter a number.")

    total = sum(numbers)
    average = total / count
    largest = max(numbers)
    smallest = min(numbers)
    even_count = sum(1 for n in numbers if n % 2 == 0)
    odd_count = count - even_count

    print("\n--- Result ---")
    print(f"Sum              : {total}")
    print(f"Average          : {average:.2f}")
    print(f"Largest number   : {largest}")
    print(f"Smallest number  : {smallest}")
    print(f"Even numbers     : {even_count}")
    print(f"Odd numbers      : {odd_count}")


if __name__ == "__main__":
    main()
