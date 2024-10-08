import sys
def pair_match(men, women):
    """
    This function receives two dictionaries in the form:
    {
        "<name>": <age>
    }

    Where <name> is a string name, and <age> is an integer representing the age.
    The function returns a pair of names (tuple) of men and women names,
    where their absolute age differences is the minimal.
    """
    minimal_diff = sys.maxsize
    man_woman_pair = ()
    for man_name, man_age in men.items():
        for woman_name, woman_age in women.items():
            abs_diff = abs(man_age - woman_age)
            if abs_diff < minimal_diff:
                minimal_diff = abs_diff
                man_woman_pair = (man_name, woman_name)
    return man_woman_pair




print(pair_match(
    {
        "John": 20,
        "Abraham": 45
    },
    {
        "July": 18,
        "Kim": 26
    }
))

# Expected ("John", "July"), since:

# abs(John - Kim) = abs(20 - 26) = abs(-6) = 6
# abs(John - July) = abs(20 - 18) = abs(2) = 2
# abs(Abraham - Kim) = abs(45 - 26) = abs(19) = 19
# abs(Abraham - July) = abs(45 - 18) = abs(27) = 27

