import pytest
from account import *


class Test:
    def setup_method(self):
        self.p1 = Account('Jimmy')
        self.p2 = Account('Jane')

    def teardown_method(self):
        del self.p1
        del self.p2

    def test_init(self):
        assert self.p1.get_name() == 'Jimmy'
        assert self.p1.get_balance() == 0
        assert self.p2.get_name() == 'Jane'
        assert self.p2.get_balance() == 0

    def test_deposit(self):
        assert self.p1.deposit(100) is True
        assert self.p1.get_balance == 100

        assert self.p1.deposit(0) is False
        assert self.p1.get_balance == 100

        assert self.p1.deposit(-30) is False
        assert self.p1.get_balance == 100

    def test_withdraw(self):
        assert self.p1.withdraw(30) is True
        assert self.p1.get_balance == 70

        assert self.p1.withdraw(-30) is False
        assert self.p1.get_balance == 70

        assert self.p1.withdraw(100) is False
        assert self.p1.get_balance == 70


