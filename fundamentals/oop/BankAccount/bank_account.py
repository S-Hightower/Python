class BankAccount:

    def __init__(self, int_rate, balance=0): 
        self.int_rate = 0.01
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance <= 0:
            print(f"Insufficient funds: Charging a $5 fee")
            self.balance -= 5 + amount
        else:
            self.balance -= amount
        return self

    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self

    def yield_interest(self):
        if self.balance <= 0:
            print(f"No interest earned.")
        else:
            self.balance += self.balance * self.int_rate
        return self

rose=BankAccount('0.01', 5000)
rose.deposit(10000).deposit(20).deposit(75).withdraw(5).yield_interest().display_account_info()

monty=BankAccount('0.01', 2000)
monty.deposit(500).deposit(50).withdraw(20).withdraw(50).yield_interest().display_account_info()