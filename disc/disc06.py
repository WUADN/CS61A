def gen_fib():
    """
    >>> next(filter(lambda x: x > 2024, gen_fib()))
    2584
    """
    n, add = 0, 1
    while True:
        yield n
        n, add = n + add, n


def differences(t):
    """Yield the differences between adjacent values from iterator t.
    >>> list(differences(iter([5, 2, -100, 103])))
    [-3, -102, 203]
    >>> next(differences(iter([39, 100])))
    61
    """
    i = next(t)
    for n in t:
        yield n - i
        i = n


def fib(big):
    n, add = 0, 1
    while True:
        if n > big:
            return n
        n, add = n + add, n


def partition_gen(n, m):
    """Yield the partitions of n using parts up to size m.
    >>> for partition in sorted(partition_gen(6, 4)):
    ...     print(partition)
    1 + 1 + 1 + 1 + 1 + 1
    2 + 1 + 1 + 1 + 1
    2 + 2 + 1 + 1
    2 + 2 + 2
    3 + 1 + 1 + 1
    3 + 2 + 1
    3 + 3
    4 + 1 + 1
    4 + 2
    """
    assert n > 0 and m > 0
    if n == m:
        yield str(m)
    if n - m > 0:
        yield from [str(m) + " + " + p for p in partition_gen(n - m, m)]
    if m > 1:
        yield from partition_gen(n, m - 1)
        
    
