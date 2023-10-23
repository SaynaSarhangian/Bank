import unittest
from customer import Customer
from bank import Bank


class TestCustomer(unittest.TestCase):
    def test_create_customer(self):
        new_customer = Customer(110)
        assert new_customer is not None

    def test_withdraw(self):
        """raises Exception due to balance of 0"""
        new_customer = Customer(110)
        with self.assertRaises(Exception):
            new_customer.withdraw(50)

    def test_deposit(self):
        new_customer = Customer(110)
        new_customer.deposit(1000)
        self.assertEqual(new_customer.balance, 1000)

    def test_get_balance(self):
        """"get_balance with no prev operations"""
        new_customer = Customer(110)
        assert new_customer.get_balance() == 0

    def test_deposit_and_withdraw(self):
        """unsuccessful withdrawal"""
        new_customer = Customer(110)
        new_customer.deposit(1000)
        with self.assertRaises(Exception):
            new_customer.withdraw(1500)


