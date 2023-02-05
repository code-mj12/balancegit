from wallet import Wallet

def test_getBalance():
  obj=Wallet(0)
  obj.set_balance(20)
  assert obj.getamount()==20

  
