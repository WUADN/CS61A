def count_partition(n, m):
    """最初版本
    >>> count_partition(6, 4)
    9
    """
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif m == 0:
        return 0
    else:
        with_m = count_partition(n - m, m)
        without_m = count_partition(n, m - 1)
        return with_m + without_m


def count_partition_match(n, m):
    """引入match, 将其中的一个递归转换为match值, 简化if条件为一个
    >>> count_partition_match(6, 4)
    9
    """
    if n < 0 or m == 0:
        return 0
    else:
        exact_match = 0
        if n == m:
            exact_match = 1
        with_m = count_partition_match(n - m, m)
        without_m = count_partition_match(n, m - 1)
        return exact_match + with_m + without_m


def list_partition(n, m):
    """list版本, 基于match改编
    >>> for i in list_partition(6, 4): print(i)
    [4, 2]
    [4, 1, 1]
    [3, 3]
    [3, 2, 1]
    [3, 1, 1, 1]
    [2, 2, 2]
    [2, 2, 1, 1]
    [2, 1, 1, 1, 1]
    [1, 1, 1, 1, 1, 1]
    """
    if n < 0 or m == 0:
        return []  # 无解，空列表
    else:
        exact_match = []
        if n == m:
            exact_match = [[m]]  # 一解
        with_m = [[m] + p for p in list_partition(n - m, m)]  # 含m的解
        without_m = list_partition(n, m - 1)  # 不需要改变
        return exact_match + with_m + without_m


def partition_str(n, m):
    """list 字符串 相加版本
    >>> for i in partition_str(6, 4): print(i)
    4 + 2
    4 + 1 + 1
    3 + 3
    3 + 2 + 1
    3 + 1 + 1 + 1
    2 + 2 + 2
    2 + 2 + 1 + 1
    2 + 1 + 1 + 1 + 1
    1 + 1 + 1 + 1 + 1 + 1
    """
    if n < 0 or m == 0:
        return []  # 无解，空列表
    else:
        exact_match = []
        if n == m:
            exact_match = [str(m)]  # 一解
        with_m = [str(m) + " + " + p for p in partition_str(n - m, m)]  # 含m的解
        without_m = partition_str(n, m - 1)  # 不需要改变
        return exact_match + with_m + without_m


def partition_str_yield(n, m):
    """list 字符串相加使用yield构造器, 大幅度简化
    你甚至可以自由选择产生多少个数字
    >>> len(list(partition_str_yield(60, 50)))
    966370
    >>> next(partition_str_yield(60, 50))
    '50 + 10'
    >>> a = 1; b = 2; True and False
    False
    >>> t = partition_str_yield(60, 50)
    >>> for _ in range(10):
    ...     print(next(t))
    50 + 10
    50 + 9 + 1
    50 + 8 + 2
    50 + 8 + 1 + 1
    50 + 7 + 3
    50 + 7 + 2 + 1
    50 + 7 + 1 + 1 + 1
    50 + 6 + 4
    50 + 6 + 3 + 1
    50 + 6 + 2 + 2
    """
    if n > 0 and m > 0:
        if n == m:
            yield str(m)  # 一解
        for p in partition_str_yield(n - m, m):  # 含m的解
            yield str(m) + " + " + p
        yield from partition_str_yield(n, m - 1)  # 不需要改变
