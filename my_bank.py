from bank import Bank
from customer import Customer

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