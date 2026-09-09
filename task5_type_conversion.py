# Task 5: What does the following code do? Explain the type conversion.
#
# Explanation:
# - "age" and "item" start out as integers (age = 20, item = 5).
# - The first two print statements display them as whole numbers: age : 20  items : 5
# - Then age = float(age) and item = float(item) CONVERT (typecast) the integer
#   values into floating-point numbers. This is called explicit type conversion,
#   done using the float() function.
# - After the conversion, the same print statements now display the values
#   with a decimal point: age : 20.0  items : 5.0
# - The values themselves don't change (20 is still "twenty"), only their
#   data type changes from int to float.

age = 20
item = 5
print("age : ", age)
print("items : ", item)

age = float(age)
item = float(item)
print("age : ", age)
print("items : ", item)
