# Statement of the CGPA Calculator Program

## Overview

This project is a simple **CGPA (Cumulative Grade Point Average)
Calculator** written in Python.\
It allows users to input their course grades and corresponding credit
values, then computes the CGPA based on predefined grade-to-point
mappings.

## Features

-   Accepts the number of courses as input.
-   Supports grade inputs: A, B, C, D, and F.
-   Validates invalid grades and invalid numeric inputs.
-   Prevents zero or negative credit values.
-   Calculates and displays CGPA rounded to two decimal places.

## Grade-to-Point Mapping

  Grade   Points
  ------- --------
  A       10
  B       8
  C       6
  D       4
  F       2

## How It Works

1.  The user specifies how many courses they have.

2.  For each course, the user enters:

    -   The grade (e.g., A, B, C)
    -   The credit value (e.g., 3.0, 4.0)

3.  The program multiplies each grade point by its credit.

4.  All points and credits are added.

5.  CGPA is calculated as:

        CGPA = Total Grade Points / Total Credits

6.  The result is printed with appropriate rounding.

## Error Handling

The program gracefully handles: - Non-numeric inputs for number of
courses and credits. - Invalid grade entries. - Zero or negative credit
values. - Zero total credits scenario.

## Purpose

This script is intended for educational purposes and helps students
quickly compute their CGPA based on simple input values.
