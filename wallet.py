class Wallet:
  def __init__(self,balance):
    self.balance=balance
  def set_balance(self,val):
    self.balance = self.balance + val
  def withdraw(self, amount):
    self.balance -= amount
  def deposit(self, amount):
    self.balance += amount
  def getamount(self):
    return self.balance
      
