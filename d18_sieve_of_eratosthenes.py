# Sieve of Eratosthenes
from math import sqrt


def eratosthenes(n):
    """Return all prime numbers up to n as a list."""
    primes = [True for _ in range(n + 1)]
    primes[0], primes[1] = False, False
    for i in range(2, int(sqrt(n))):
        if primes[i]:
            j = 2
            while i * j <= n:
                primes[i * j] = False
                j += 1
    return [x for x in range(n + 1) if primes[x]]


print(eratosthenes(30))  # -> [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
