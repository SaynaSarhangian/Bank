import unittest
from bank import Bank
from customer import Customer


class TestBank(unittest.TestCase):
    def test_add_customer(self):
        b1 = Bank()
        c1 = Customer(110)
        b1.add_customer(c1)
        assert b1.customers[0] == c1

    def test_deposit_operation(self):
        """test with existing customer"""
        b1 = Bank()
        c1 = Customer(110)
        b1.add_customer(c1)
        b1.deposit_operation(110, 1000)
        self.assertEqual(b1.bank_balance, 1000)
