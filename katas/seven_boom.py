def seven_boom(n):
    """
    This functions returns a list of all "Booms" for a 7-boom play starting from 1 to n
    """
    all_booms = []
    for i in range(1, n+1):
        if "7" in str(i) or i % 7 == 0:
            all_booms.append(i)
    return all_booms


print(seven_boom(35))  # Expected [7, 14, 17, 21, 27, 28]

