class Customer:

    def __init__(self, account_id):
        self.account_id = account_id
        self.balance = 0

    def withdraw(self, withdraw_amount):
        if withdraw_amount > self.balance:
            print(f'Abort! withdraw_amount {withdraw_amount} cannot be greater than balance {self.balance}')
            raise Exception('Invalid amount!')
        else:
            self.balance -= withdraw_amount
            print(
                f'success! ${withdraw_amount} was withdrawn from your account. your balance now is ${self.balance}')

    def deposit(self, deposit_amount):
        self.balance += deposit_amount

    def get_balance(self):
        return self.balance


class Bank:
    def __int__(self, bank_balance=0):
        pass


if __name__ == '__main__':
    cus1 = Customer(12)
    cus1.deposit(2600)
    cus1.withdraw(1000)
    customer_balance = cus1.get_balance()
    print(customer_balance)
