class Account:
    """
    A class for creating and manipulating bank accounts and amount held within.
    """
    def __init__(self, name: str, balance=0.0) -> None:
        """
        Constructor to create initial state of an account object
        :param name: The account holder's name.
        :param balance: The amount of money within the person's account.
        """
        self.__account_name = name
        self.__account_balance = balance

    def deposit(self, amount: float) -> bool:
        """
        Method to increase a person's account_balance.
        :param amount: Amount to be added to the account_balance.
        :return: Boolean to represent the success or failure of the transaction.
        """
        if amount <= 0:
            return False
        elif amount > 0:
            self.__account_balance += amount
            return True

    def withdraw(self, amount: float) -> bool:
        """
        Method to decrease a person's account_balance.
        :param amount: Amount to be deducted from the account_balance.
        :return: Boolean to represent the success or failure of the transaction.
        """
        if amount <= 0 or amount > self.__account_balance:
            return False
        elif amount <= self.__account_balance:
            self.__account_balance -= amount
            return True

    def get_balance(self) -> float:
        """
        Method to access an account's current balance.
        :return: The current balance within the account.
        """
        return self.__account_balance

    def get_name(self) -> str:
        """
        Method to access an account holder's name
        :return: The account holder's name.
        """
        return self.__account_name


