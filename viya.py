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
