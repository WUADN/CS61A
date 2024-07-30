empty = "empty"
"""以下是 linked list的构造器与选择器"""


def is_link(s):
    return len(s) == 0 or (len(s) == 2 and is_link(s[1]))


def link(first, rest):
    assert is_link(rest), "rest must be a link"
    return [first, rest]


def first(s):
    assert is_link, "first can only used in link list"
    assert s != empty, "empty link list has not first element"
    return s[0]


def rest(s):

    assert is_link, "first can only used in link list"
    assert s != empty, "empty link list has not first element"
    return s[1]


"""下面是基于第一层抽象屏障的基础功能实现"""


def len_link(s):
    """return lenght of linked_list"""
    length = 0
    while s != empty:
        s, length = rest(s), length + 1
    return length


def len_link_recursive(s):
    return len_link_recursive_helper(s, 0)  # or return len_link_recursive(rest) + 1


def len_link_recursive_helper(s, l):
    if s == empty:
        return l
    return len_link_recursive_helper(rest(s), l + 1)


def getitem_link(s, i):
    """return the element of linked list which index is i"""
    while i > 0:
        s, i = rest(s), i - 1
        return first(s)
