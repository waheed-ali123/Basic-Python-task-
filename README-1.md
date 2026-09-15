# Question No2 - Advanced Student Marksheet

**Author:** Waheed Ali
**Roll No:** 96

A Python program that creates an advanced student marksheet.

## Features
1. Asks the user to enter the student's name and roll number.
2. Inputs marks for 5 subjects.
3. Calculates the total marks and percentage.
4. Determines the grade according to:
   - 80-100% -> A+
   - 70-79%  -> A
   - 60-69%  -> B
   - 50-59%  -> C
   - 40-49%  -> D
   - Below 40% -> F
5. Checks whether the student passed or failed.
6. If the student scores below 40 in any single subject, the student is
   declared a Fail regardless of the overall percentage.
7. Displays a complete marksheet containing the student's information:
   name, roll no, subject marks, total, percentage, grade, and result.

## How to Run
```
python marksheet.py
```

## Example
```
Enter student's name: John Doe
Enter roll number: 101
Enter name of Subject 1: Math
Enter marks for Math (out of 100): 85
...

===================================
           STUDENT MARKSHEET
===================================
Name        : John Doe
Roll No     : 101
-----------------------------------
Subject             Marks
-----------------------------------
Math                85.0
...
-----------------------------------
Total Marks : 400.00 / 500
Percentage  : 80.00%
Grade       : A+
Result      : Pass
===================================
```
