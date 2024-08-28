def count_times(f):
    """计算函数调用次数
    Args:
        f : 被装饰函数
    >>> fib = count(fib)
    >>> fib(5)
    5
    >>> fib.call_count
    15
    >>> fib(30)
    832040
    >>> fib.call_count
    2692552
    """

    def counted(n):
        counted.call_count += 1
        return f(n)

    counted.call_count = 0
    return counted


def count_frames(f):
    def counted(n):
        counted.open_count += 1
        if counted.open_count > counted.max_count:
            counted.max_count = counted.open_count
        result = f(n)
        counted.open_count -= 1
        return result

    counted.open_count = 0
    counted.max_count = 0
    return counted


def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


def memo(f):
    cache = {}

    def memoized(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]

    return memoized
