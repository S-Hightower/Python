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

# guido.make_deposit(100).make_deposit(350).make_deposit(200).make_withdrawal(50)
# print(guido.account_balance)

# monty.make_deposit(500).make_deposit(500).make_withdrawal(100).make_withdrawal(300)
# print(monty.account_balance)

# rose.make_deposit(10000).make_withdrawal(20).make_withdrawal(75).make_withdrawal(5).display_user_balance()
# print(rose.account_balance)