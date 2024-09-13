def can_drive(age, has_license):
    """
    Determines if a person is eligible for a discount based on their age, license status, and student status.
    """
    eligible_to_drive = (age >= 18 and age < 65) or has_license
    if eligible_to_drive:
        return "You can drive."
    return "You cannot drive."


result = can_drive(17, True)
print(result)  # Expected output: You can drive.

result = can_drive(25, True)
print(result)  # Expected output: You can drive.

result = can_drive(17.9, False)
print(result)  # Expected output: You cannot drive.

result = can_drive(70, True)
print(result)  # Expected output: You can drive.

"""
To complete this exercise:
--------------------------
Implement the 'can_drive' function to check if a person is eligible to drive. 
The function should return a message indicating if the person meets both conditions: being at least 18 and under 65 years old or already have a valid license.


Exercise Breakdown:
-------------------
The `or` operator in Python is used to combine multiple conditions.
It returns `True` if one condition is true and `False` if all conditions are false.

Parentheses are used to group conditions and control the order of evaluation when using `and` and `or` operators. 
"""
