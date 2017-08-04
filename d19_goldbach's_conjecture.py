# Goldbach's conjecture
from d18_sieve_of_eratosthenes import eratosthenes
from d03_binary_search import binary_search


def prime_sum(n, primes):
    """Return two primes that add up to n."""
    if n <= 2 or n % 2 != 0:
        return

    i = 0
    while primes[i] <= n / 2:
        difference = n - primes[i]
        if binary_search(primes, difference)[0]:
            return f"{primes[i]} + {difference} = {n}"
        i += 1


if __name__ == '__main__':
    print(prime_sum(4, eratosthenes(10000)))  # 2 + 2 = 4
    print(prime_sum(64, eratosthenes(10000)))  # 3 + 61 = 64
    print(prime_sum(720, eratosthenes(10000)))  # 11 + 709 = 720
