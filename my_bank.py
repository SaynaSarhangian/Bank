from typing import List


class Customer:

    def __init__(self, account_id: int):
        self.account_id = account_id
        self.balance = 0

    def withdraw(self, withdraw_amount: int):
        if withdraw_amount > self.balance:
            print(f'Abort! withdraw_amount {withdraw_amount} cannot be greater than balance {self.balance}')
            raise Exception('Invalid amount!')
        else:
            self.balance -= withdraw_amount
            print(
                f'success! ${withdraw_amount} was withdrawn from your account. your balance now is ${self.balance}')

    def deposit(self, deposit_amount: int):
        self.balance += deposit_amount

    def get_balance(self):
        return self.balance


class Bank:
    def __init__(self, bank_balance: int = 0):
        self.bank_balance = bank_balance
        self.customers: List[Customer] = []

    def add_customer(self, customer_obj: Customer):
        self.customers.append(customer_obj)

    def get_bank_balance(self):
        return self.bank_balance

    def deposit_operation(self, id, amount):
        self.bank_balance += amount
        for item in self.customers:
            if item.account_id == id:
                item.deposit(amount)



if __name__ == '__main__':
    # cus1.deposit(2600)
    # cus1.withdraw(1000)
    # customer_balance = cus1.get_balance()
    # print(customer_balance)
    b1 = Bank()
    cus1 = Customer(1220)
    b1.add_customer(cus1)
    print(b1.get_bank_balance())
    b1.deposit_operation(1220, 1000)
    print(b1.get_bank_balance())