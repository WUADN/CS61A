from tree_by_func import *


def fib_tree(n):
    if n == 0 or n == 1:
        return tree(n)
    left, right = fib_tree(n - 2), fib_tree(n - 1)
    fib_n = label(left), label(right)
    return tree(fib_n, [left, right])


def count_tree(tree):
    if is_leaf(tree):
        return 1
    else:
        sum = 0
        for branch in branches(tree):
            sum += count_tree(branch)
        return sum


def count_tree_list(tree):
    if is_leaf(tree):
        return 1
    else:
        branch_count = [count_tree_list(b) for b in branches(tree)]
        return sum(branch_count)
