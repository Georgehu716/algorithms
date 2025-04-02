def fib_recursive(n: int) -> int:
    if n < 2:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)


def fib_memoized(n: int) -> int:
    """
    Store previously calculated value.
    """
    if n < 2:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


for i in range(10):
    print(fib_recursive(i), end=" ")
print()
for i in range(10):
    print(fib_memoized(i), end=" ")
