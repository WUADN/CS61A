from trees import *


def has_path(t, p):
    """Return whether tree t has a path from the root with labels p.
    主要是注意p列表的更新以及遍历关系，一baseline len(p) == 1 is ok
    >>> t2 = tree(5, [tree(6), tree(7)])
    >>> t1 = tree(3, [tree(4), t2])
    >>> has_path(t1, [5, 6]) # This path is not from the root of t1
    False
    >>> has_path(t2, [5, 6]) # This path is from the root of t2
    True
    >>> has_path(t1, [3, 5]) # This path does not go to a leaf, but that's ok
    True
    >>> has_path(t1, [3, 5, 6]) # This path goes to a leaf
    True
    >>> has_path(t1, [3, 4, 5, 6]) # There is no path with these labels
    False
    """
    if p == [label(t)]:  # when len(p) is 1
        return True
    elif label(t) != p[0]:
        # print(t, label(t))
        return False
    else:
        for branch in branches(t):
            if has_path(branch, p[1:]):
                return True
        return False


def find_path(t, x):
    """
    同样是遍历branches，组合路径
    >>> t2 = tree(5, [tree(6), tree(7)])
    >>> t1 = tree(3, [tree(4), t2])
    >>> find_path(t1, 5)
    [3, 5]
    >>> find_path(t1, 4)
    [3, 4]
    >>> find_path(t1, 6)
    [3, 5, 6]
    >>> find_path(t2, 6)
    [5, 6]
    >>> print(find_path(t1, 2))
    None
    """
    if x == label(t):
        return [x]
    for branch in branches(t):
        path = find_path(branch, x)
        if path:
            return [label(t)] + path
    return None


if __name__ == "__main__":
    import doctest

    doctest.testmod()
