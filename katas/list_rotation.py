def rotate_list(lst, n):
    """
    Rotates the list 'lst' by 'n' positions to the right.
    """
    rotated_list = lst.copy()
    if n > 0 :
        for i in range(n):
            rotated_list.insert(0,rotated_list.pop())
    else:
        for i in range(abs(n)):
            rotated_list.insert(len(rotated_list),rotated_list.pop(0))
    return rotated_list



original_list = [1, 2, 3, 4, 5]
result = rotate_list(original_list, 2)
print(result)  # Expected output: [4, 5, 1, 2, 3]

result = rotate_list(original_list, -1)
print(result)  # Expected output: [2, 3, 4, 5, 1]

result = rotate_list(original_list, 0)
print(result)  # Expected output: [1, 2, 3, 4, 5]

"""
To complete this exercise:
--------------------------
Ensure that the rotation handles both positive and negative values of 'n'.


Exercise Breakdown:
-------------
You can use a for loop with the range() function to iterate over the indices of a list.
The `%` operator can also help.
"""
