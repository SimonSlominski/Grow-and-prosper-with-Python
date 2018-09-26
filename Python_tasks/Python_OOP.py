"""Object Oriented Programming Challenge

Create a bank account class that has two attributes:
owner
balance

and two methods:
deposit
withdraw

Additional requirement: withdrawals may not exceed the available balance.
"""

class Account:

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f"Account owner:\t{self.owner}\nAccount balance:  ${self.balance}"

    def deposit(self, deposit_amount):
        self.balance += deposit_amount
        print("Deposit Accepted")
        return f"Account balance: ${self.balance}"

    def withdraw(self, withdraw_amount):
        if self.balance >= withdraw_amount:
            self.balance -= withdraw_amount
            print("Withdrawal accepted")
            return f"Account balance: ${self.balance}"
        else:
            print("Withdrawal unavailabe!")