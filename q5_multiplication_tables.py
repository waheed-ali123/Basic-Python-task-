"""
Question No5
Ask the user for a number n and print multiplication tables from 1 to n.
"""

def main():
    while True:
        try:
            n = int(input("Enter a number n: "))
            if n > 0:
                break
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

    for table in range(1, n + 1):
        print(f"\nMultiplication table of {table}:")
        for i in range(1, 11):
            print(f"{table} x {i} = {table * i}")


if __name__ == "__main__":
    main()
