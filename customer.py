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
