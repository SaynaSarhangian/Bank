from typing import List

from customer import Customer


class Bank:
    def __init__(self, bank_balance: int = 0):
        self.bank_balance = bank_balance
        self.customers: List[Customer] = []

    def _find_customer(self, id) -> Customer:  # defining the returned data type (class Customer)
        """

        :param id: customer id
        :return: an instance of class Customer
        """
        for customer in self.customers:
            if customer.account_id == id:
                return customer
        raise Exception(f'customer {id} was not found!')

    def add_customer(self, customer: Customer):
        self.customers.append(customer)

    def get_bank_balance(self):
        return self.bank_balance

    def deposit_operation(self, id, amount):
        self.bank_balance += amount
        customer = self._find_customer(id)
        customer.deposit(amount)

    def withdraw_operation(self, id, amount):
        customer = self._find_customer(id)
        customer.withdraw(amount)
        self.bank_balance -= amount
