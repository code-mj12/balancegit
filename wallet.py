class Wallet:
  def __init__(self,balance):
    self.balance=balance
   def set_balance(balance):
    self.balance = balance
   def withdraw(self, amount):
        self.balance -= amount
   def deposit(self, amount):
        self.balance += amount
      
# create an object of class wallet and set balance to 1000
wallet = Wallet(1000)
# print the balance
print(wallet.balance)
# withdraw 500
wallet.withdraw(500)
# print the balance
print(wallet.balance)
# deposit 1000
wallet.deposit(1000)
# print the balance 
print(wallet.balance)
