class BankAccount:
    def __init__(self, balance=0):
        self.__balance = balance  # Private attribute
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Invalid withdrawal amount.")
    
    def get_balance(self):
        return self.__balance

# # Create a BankAccount object
account = BankAccount(100)
account.deposit(50)    # Balance: 150
account.withdraw(30)   # Balance: 120
print(account.get_balance())  # Output: 120
