class BankAccount:

    def __init__(self, accno, balance):
        self.accno = accno
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Amount Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            print("Amount Withdrawn:", amount)
        else:
            print("Insufficient Balance")

    def display(self):
        print("Account Number:", self.accno)
        print("Balance:", self.balance)


b1 = BankAccount(12345, 10000)

b1.deposit(2000)
b1.withdraw(3000)
b1.display()
