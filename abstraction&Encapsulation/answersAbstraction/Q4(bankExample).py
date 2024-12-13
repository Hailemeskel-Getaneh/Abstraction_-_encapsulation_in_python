from abc import ABC, abstractmethod

# Abstract class
class BankAccount(ABC):
    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

# Concrete class
class SavingsAccount(BankAccount):
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. Current balance: {self.balance}")
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. Current balance: {self.balance}")
        else:
            print("Insufficient funds.")

# Testing the SavingsAccount class
account = SavingsAccount(500)
account.deposit(200)
account.withdraw(100)
account.withdraw(700)
