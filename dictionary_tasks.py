# Lab Task 1: Dictionaries

# Question 1: Count occurrences of each number (without count())
print("Question 1")
numbers = [2, 3, 2, 5, 3, 2, 5, 8]
counts = {}
for n in numbers:
    if n in counts:
        counts[n] += 1
    else:
        counts[n] = 1
print(counts)  # {2: 3, 3: 2, 5: 2, 8: 1}

# Question 2: Print every student with the highest marks
print("\nQuestion 2")
marks = {'Ali': 85, 'Sara': 95, 'Ahmed': 95, 'Noor': 78}
highest = max(marks.values())
for name, mark in marks.items():
    if mark == highest:
        print(name, mark)

# Question 3: Swap keys and values
print("\nQuestion 3")
data = {'a': 1, 'b': 2, 'c': 3}
swapped = {}
for key, value in data.items():
    swapped[value] = key
print(swapped)  # {1: 'a', 2: 'b', 3: 'c'}

# Question 4: Group words by first letter (loops and conditions)
print("\nQuestion 4")
words = ['apple', 'ant', 'banana', 'ball', 'cat']
grouped = {}
for word in words:
    first = word[0]
    if first in grouped:
        grouped[first].append(word)
    else:
        grouped[first] = [word]
print(grouped)  # {'a': ['apple', 'ant'], 'b': ['banana', 'ball'], 'c': ['cat']}
