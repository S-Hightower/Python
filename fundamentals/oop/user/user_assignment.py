class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    
    def make_deposit(self, amount):
    	self.account_balance += amount

    def make_withdrawal(self, amount):
        self.account_balance -= amount

    def display_user_balance(self):
         print(f"User: {self.name}, Balance: {self.account_balance}")
         return self

guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
rose = User("Rose Black", "rose@python.com")

# guido.make_deposit(100)
# guido.make_deposit(350)
# guido.make_deposit(200)
# guido.make_withdrawal(50)
# print(guido.account_balance)

# monty.make_deposit(500)
# monty.make_deposit(500)
# monty.make_withdrawal(100)
# monty.make_withdrawal(300)
# print(monty.account_balance)

# rose.make_deposit(10000)
# rose.make_withdrawal(20)
# rose.make_withdrawal(75)
# rose.make_withdrawal(5)
# print(rose.account_balance)
# rose.display_user_balance()