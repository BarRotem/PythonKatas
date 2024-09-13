def can_drive(age, has_license):
    """
    Determines if a person can drive based on their age and license status.
    """
    eligible_to_drive = age >= 18 and has_license
    if eligible_to_drive:
        return "You can drive."
    return "You cannot drive."



result = can_drive(20, True)
print(result)  # Expected output: You can drive.

result = can_drive(16, True)
print(result)  # Expected output: You cannot drive.

result = can_drive(22, False)
print(result)  # Expected output: You cannot drive.

result = can_drive(17, False)
print(result)  # Expected output: You cannot drive.

"""
To complete this exercise:
--------------------------
Implement the 'can_drive' function to check if a person is eligible to drive. The function should return a message 
indicating if the person meets both conditions: being at least 18 years old and having a valid license.


Exercise Breakdown:
-------------------
The `and` operator in Python is used to combine multiple conditions.
It returns `True` if all conditions are true and `False` otherwise.
This allows you to perform checks that require multiple criteria to be met.

if x == 6 and y > 9:
    print('...')
"""
