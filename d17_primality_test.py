# Primality test

from math import sqrt

def is_prime(n):
    """Check if integer n is a prime."""
    if n <= 1:
        return False
    if n % 2 == 0 and n > 2 or n <= 1:
        return False
    return all(n % i for i in range(3, int(sqrt(n)) + 1, 2))


print(is_prime(15))  # -> False
print(is_prime(97169))  # -> True
