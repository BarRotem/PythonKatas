def prime_number(num):
    """
    Check if the given number is prime or not.
    """
    for i in range(2, num-1):
        if num % i == 0 :
            return False
    return True


print(prime_number(5))  # True
print(prime_number(22))  # False

"""
To complete this exercise:
--------------------------
A prime number is an integer greater than 1 that cannot be divided by any other numbers except 1 and itself. 

Examples of prime numbers are 2, 3, 5, 7, 11, 13, etc.
 
A number is **not prime** if it can be divided evenly by another number (other than 1 and itself).
"""
