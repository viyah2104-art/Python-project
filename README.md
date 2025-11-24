#  CGPA Calculator (Python)

## 📌 Overview

This project is a simple **CGPA (Cumulative Grade Point Average)
Calculator** built using Python.\
It allows users to enter their course grades and corresponding credit
values, then computes the CGPA based on a predefined grade-to-point
mapping system.

## ✨ Features

-   Asks the user for the number of courses.
-   Accepts grades: **A, B, C, D, F**.
-   Validates invalid grade entries.
-   Validates credit values to avoid invalid or negative inputs.
-   Outputs CGPA rounded to **two decimal places**.
-   Handles common input errors gracefully.

## 📊 Grade-to-Point Mapping

  Grade   Points
  ------- --------
  A       10
  B       8
  C       6
  D       4
  F       2

## 🧮 How the Program Works

1.  User enters how many courses they have.

2.  For each course:

    -   The user inputs the grade.
    -   The user inputs the credit value.

3.  The program calculates:

        CGPA = Total Grade Points Earned / Total Credits

4.  Displays the final CGPA rounded to 2 decimals.

## 🧱 Code Snippet

``` python
def calculate_cgpa():
    grade_points = {
        'A': 10,
        'B': 8,
        'C': 6,
        'D': 4,
        'F': 2
    }

    total_points = 0
    total_credits = 0

    try:
        n = int(input("How many courses? "))
    except:
        print("Please enter a number.")
        return

    if n <= 0:
        print("Number of courses should be more than 0.")
        return

    for i in range(1, n + 1):
        grade = input(f"Grade for course {i}: ").upper().strip()
        if grade not in grade_points:
            print("Wrong grade entered.")
            return

        try:
            credit = float(input(f"Credits for course {i}: "))
        except:
            print("Invalid credit value.")
            return

        if credit <= 0:
            print("Credits can’t be zero or negative.")
            return

        total_points += grade_points[grade] * credit
        total_credits += credit

    if total_credits == 0:
        print("No credits found.")
        return

    cgpa = total_points / total_credits
    print("CGPA =", round(cgpa, 2))


calculate_cgpa()
```

## 🎯 Purpose

This script is ideal for students or beginners learning: - CGPA
calculation logic\
- Python input/output\
- Basic validation\
- Simple weighted average formulas

## 📁 Files Included

-   `statement.md`
-   `cgpa_calculator.py`
-   `README.md`

