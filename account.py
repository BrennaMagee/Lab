class Account:

    def __init__(self, name):
        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount):
        pass

    def withdraw(self, amount):
        pass

    def get_balance(self):
        return self.__account_balance

    def get_name(self):
        return self.__account_name


