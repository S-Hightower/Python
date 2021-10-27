class BankAccount:

    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance <= 0:
            print(f"Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        else:
            self.balance -= amount
        return self

    def display_account_info(self):
        return (f"{self.balance}")

    def yield_interest(self):
        if self.balance <= 0:
            print(f"No interest earned.")
        else:
            self.balance += self.balance * self.int_rate
        return self

class User:
    def __init__(self, name,):
        self.name = name
        self.account = BankAccount(0.01,balance = 0)

    def display_user_balance(self):
         print(f"User: {self.name}, Balance: {self.account.display_account_info()}")
         return self

guido = User("Guido van Rossum")
monty = User("Monty Python")
rose = User("Rose Black")

rose.account.deposit(10000)
rose.display_user_balance()