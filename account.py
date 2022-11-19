class Account:

    def __init__(self, name: str) -> None:
        self.__account_name: str = name
        self.__account_balance: float = 0

    def deposit(self, amount: float) -> bool:
        if amount <= 0:
            return False
        elif amount > 0:
            self.__account_balance += amount
            return True

    def withdraw(self, amount: float) -> bool:
        if amount <= 0 or amount > self.__account_balance:
            return False
        elif amount <= self.__account_balance:
            self.__account_balance -= amount
            return True

    def get_balance(self) -> float:
        return self.__account_balance

    def get_name(self) -> str:
        return self.__account_name

