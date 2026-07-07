class BankAccount:

    def __init__(self, balance):

        self.balance = balance

    def deposit(self, amount):

        self.balance += amount

    def withdraw(self, amount):

        if amount <= self.balance:

            self.balance -= amount

        else:

            print("Insufficient Balance")

    def show_balance(self):

        print("Balance =", self.balance)

account = BankAccount(10000)

account.deposit(2000)
account.withdraw(3000)

account.show_balance()