# Lab Task 2: Sets

# Question 1: Set of five fruits
print("Question 1")
fruits = {"apple", "banana", "mango", "orange", "grape"}
print(fruits)

# Question 2: Remove duplicates from a list
print("\nQuestion 2")
numbers = [2, 4, 2, 6, 4, 8, 8]
unique_numbers = set(numbers)
print(unique_numbers)  # {2, 4, 6, 8}

# Question 3: Add 10 and remove one existing number
print("\nQuestion 3")
nums = {1, 2, 3, 4, 5}
nums.add(10)
nums.remove(3)
print(nums)  # {1, 2, 4, 5, 10}

# Question 4: Check if user's number exists in the set
print("\nQuestion 4")
s = {10, 20, 30, 40, 50}
user_num = int(input("Enter a number: "))
if user_num in s:
    print(user_num, "exists in the set")
else:
    print(user_num, "does not exist in the set")

# Question 5: Length of a set with duplicates
print("\nQuestion 5")
values = {1, 2, 2, 3, 3, 3, 4}
print(len(values))  # 4
# Explanation: sets store only unique elements, so duplicates are
# ignored. The set becomes {1, 2, 3, 4}, which has 4 elements.

# Question 6: Set operations
print("\nQuestion 6")
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print("Union (A | B):", A | B)                    # {1, 2, 3, 4, 5, 6}
print("Intersection (A & B):", A & B)             # {3, 4}
print("A - B:", A - B)                            # {1, 2}
print("B - A:", B - A)                            # {5, 6}
# A - B and B - A differ because difference keeps only the elements
# that belong to the first set and not to the second.
print("Symmetric difference (A ^ B):", A ^ B)     # {1, 2, 5, 6}
