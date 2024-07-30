class Account:
    interest = 0.02  # 类属性

    @classmethod
    def change_class_attr(cls):
        cls.interest += 0.02

    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder

    # 在这里定义更多的方法
    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        self.balance = self.balance - amount
        return self.balance


def normal(c):
    c.interest += 0.02
    print(c.interest)
