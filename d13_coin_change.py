# Dynamic programming coin change problem


def coin_change(coins, n):
    """
    Returns the minimum amount of coins to get the sum of n.
    Recursive solution.
    coins is a tuple or list
    n is the sum to get
    """
    values = {}  # cached results

    def solve(x):
        if x < 0:
            return float("inf")
        elif x == 0:
            return 0
        elif x in values:
            return values[x]
        best = float("inf")
        for c in coins:
            best = min(best, solve(x - c) + 1)
        values[x] = best
        return best

    return solve(n)


def coin_change2(coins, n):
    """
    Returns the minimum amount of coins to get the sum of n.
    Iterative solution.
    coins is a tuple or list
    n is the sum to get
    """
    v = [0] * (n + 1)

    def iterative():
        for x in range(1, len(v)):
            v[x] = float("inf")
            for c in coins:
                if x - c >= 0:
                    v[x] = min(v[x], v[x - c] + 1)
        return v

    return iterative()[n]


def coin_change3(coins, n):
    """
    Returns the minimum amount of coins and the solution to get the sum of n
    as a tuple -> (minimum amount (int), solution (list of ints))
    Iterative solution.
    coins is a tuple or list
    n is the sum to get
    """
    v = [0] * (n + 1)
    first = [0] * (n + 1)

    for x in range(1, len(v)):
        v[x] = float("inf")
        for c in coins:
            if x - c >= 0 and v[x - c] + 1 < v[x]:
                v[x] = v[x - c] + 1
                first[x] = c

    result = v[n]
    solution = []
    while n > 0:
        solution.append(first[n])
        n -= first[n]
    return result, solution


def count_ways(coins, n):
    """
    Return the count of possible ways to get a sum of n with coins.
    coins is a tuple or list
    n is the sum to get
    """
    ways = [1] + [0] * n
    for c in coins:
        for i in range(c, n + 1):
            ways[i] += ways[i - c]
    return ways[n]


N = 11
COINS = (1, 3, 4)
print(coin_change(COINS, N))  # -> 3
print(coin_change2(COINS, N))  # -> 3
print(coin_change3(COINS, N))  # -> (3, [3, 4, 4])
print(count_ways(COINS, N))  # -> 9
