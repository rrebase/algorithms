# Implementations of generating fibonacci numbers


def fib_1(n):
    """Recrusive solution."""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fib_1(n - 1) + fib_1(n - 2)


def fib_2(n):
    """Iterative solution."""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    fibo_prev, fibo = 0, 1
    for i in range(2, n):
        fibo_prev, fibo = fibo, fibo_prev + fibo
    return fibo + fibo_prev


def fib_3(x):
    """Recursive, cache values."""
    d = {}

    def f(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        if n in d:
            return d.get(n)
        d[n] = f(n - 1) + f(n - 2)
        return d[n]
    return f(x)


print(fib_1(10))  # -> 55
print(fib_2(70))  # -> 190392490709135
print(fib_3(70))  # -> 190392490709135
