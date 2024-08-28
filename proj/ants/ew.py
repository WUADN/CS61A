# 首先使用高阶函数定义通用的函数概念
def improve(update, close, guess=1):
    while not close(guess):
        guess = update(guess)
    return guess


# 我们使用原始函数作为参数，构造出具体的更新函数，然后返回
def newton_update(f, df):
    def update(x):
        return x - f(x) / df(x)

    return update


# 同上，接收函数，组合函数，返回函数
def find_zero(f, df):
    def near_zero(x):
        return approx_eq(f(x), 0)

    return improve(newton_update(f, df), near_zero)


def square_root_newton(a):  # 这里我们通过嵌套函数扩展了函数参数的接收个数
    def f(x):
        return x * x - a

    def df(x):
        return 2 * x

    return find_zero(f, df)


# 我们推广到n次方根
def power(x, n):
    """返回 x * x * x * ... * x，n 个 x 相乘"""
    product, k = 1, 0
    while k < n:
        product, k = product * x, k + 1
    return product


def approx_eq(x, y, tolerance=1e-15):
    return abs(x - y) < tolerance


def nth_root_of_a(n, a):
    def f(x):
        return power(x, n) - a

    def df(x):
        return n * power(x, n - 1)

    return find_zero(f, df)


if __name__ == "__main__":
    print(f"square_root_newton(64) is {square_root_newton(64)}")
    print(f"nth_root_of_a(2, 64) is {nth_root_of_a(2, 64)}")
    print(f"nth_root_of_a(6, 64) is {nth_root_of_a(3, 64)}")
    print(f"nth_root_of_a(6, 64) is {nth_root_of_a(6, 64)}")
