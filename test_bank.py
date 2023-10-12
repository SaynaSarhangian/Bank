import unittest

from Bank.my_bank_revised import Customer


class TestBank(unittest.TestCase):
    def test_create_customer(self):
        new_customer = Customer(110)
        assert new_customer is not None

