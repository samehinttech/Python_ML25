"""
This script demonstrates the use of logical operators in conditional statements.
It includes examples of 'and', 'or', and 'not' operators.

- 'and' operator: True if both conditions are true.
- 'or' operator: True if at least one condition is true.
- 'not' operator: Inverts the truth value of a condition.
"""

# Example of student admission based on grades and attendance
grade = 85
attendance = 90
min_grade = 80
min_attendance = 75
if grade >= min_grade and attendance >= min_attendance:
    print("Student is eligible for admission.")
else:
    print("Student is not eligible for admission.")


# Example of attend the exam based on having the student card or the ID card
has_student_card = True
has_id_card = False
if has_student_card or has_id_card:
    print("Student can attend the exam.")
else:
    print("Student needs to present a valid card to attend the exam.")


# Example of checking if a number is not in a specific range
number = 15
if not (10 <= number <= 20):
    print("Number is outside the range of 10 to 20.")
else:
    print("Number is within the range of 10 to 20.")


# Example of a complex condition using all three logical operators
age = 22
has_permission = True
if (age >= 18 and has_permission) or (age < 18 and not has_permission):  #
    # The second condition is nonsensical but for demonstration only.
    print("Access granted.")
else:
    print("Access denied.")