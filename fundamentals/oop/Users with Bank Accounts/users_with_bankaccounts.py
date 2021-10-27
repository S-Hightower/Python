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

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = 0
    
    def make_deposit(self, amount):
    	self.account += amount

    def make_withdrawal(self, amount):
        self.account -= amount

    def display_user_balance(self):
         print(f"User: {self.name}, Balance: {self.account}")
         return self

guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
rose = User("Rose Black", "rose@python.com")