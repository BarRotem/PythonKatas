def monotonic_array(lst):
    """
    This function returns True/False if the given list is monotonically increased or decreased
    """
    inc = True
    dec = True
    for i in range(1, len(lst)):
        if lst[i] > lst[i-1] and inc == True:
            inc = True
            dec = False
        elif lst[i] < lst[i-1] and dec == True:
            inc = False
            dec = True
        elif lst[i] != lst[i-1]:
            return False
    return inc or dec




print(monotonic_array([1, 2, 3, 6, 8, 9, 0]))  # False
print(monotonic_array([1, 2, 2, 2, 8, 9, 10]))  # True
print(monotonic_array([1, 2, 2, 3, 2, 2, 1]))  # True
print(monotonic_array([1, 2, 1, 2, 3]))  # True
print(monotonic_array([1, 2, 3, 4]))  # True
