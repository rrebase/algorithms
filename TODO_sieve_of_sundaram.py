# Sieve of Sundaram


def sundaram(n):
    """Return all prime numbers up to n as a list."""
    n_half = (n - 1) // 2
    arr = list(range(n_half + 1))
    i = 1
    while True:
        step = 2 * i + 1
        start = i * (step + 1)
        if start > n_half:
            break
        arr[start::step] = (0 for i in range(start, n_half + 1, step))
        i += 1
    return [2] + [2 * k + 1 for k in filter(None, arr)]


print(sundaram(30))  # -> [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
