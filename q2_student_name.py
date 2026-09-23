"""
Question No2
Take a student's name and display:
- Name in uppercase
- Name in lowercase
- Number of characters
- First character
- Last character
"""

def main():
    name = input("Enter student's name: ").strip()

    while name == "":
        name = input("Name cannot be empty. Enter student's name: ").strip()

    print("\n--- Result ---")
    print(f"Uppercase        : {name.upper()}")
    print(f"Lowercase        : {name.lower()}")
    print(f"Number of chars  : {len(name)}")
    print(f"First character  : {name[0]}")
    print(f"Last character   : {name[-1]}")


if __name__ == "__main__":
    main()
