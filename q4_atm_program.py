"""
Question No4
A simple ATM program.
Start with Balance = 50000
Menu:
1. Check Balance
2. Deposit
3. Withdraw
4. Exit
Loop until the user selects Exit.
"""

def main():
    balance = 50000

    while True:
        print("\n===== ATM MENU =====")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Select an option (1-4): ").strip()

        if choice == "1":
            print(f"Your current balance is: {balance}")

        elif choice == "2":
            try:
                amount = float(input("Enter amount to deposit: "))
                if amount <= 0:
                    print("Deposit amount must be positive.")
                else:
                    balance += amount
                    print(f"Deposit successful. New balance: {balance}")
            except ValueError:
                print("Invalid amount.")

        elif choice == "3":
            try:
                amount = float(input("Enter amount to withdraw: "))
                if amount <= 0:
                    print("Withdrawal amount must be positive.")
                elif amount > balance:
                    print("Insufficient balance.")
                else:
                    balance -= amount
                    print(f"Withdrawal successful. New balance: {balance}")
            except ValueError:
                print("Invalid amount.")

        elif choice == "4":
            print("Thank you for using the ATM. Goodbye!")
            break

        else:
            print("Invalid choice. Please select 1-4.")


if __name__ == "__main__":
    main()
