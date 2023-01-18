from bank_account import BankAccount

def test_bank_account_creation():
   account = BankAccount("Greg")
   account_2 = BankAccount("John")
   assert account.name == "Greg"
   assert account.balance == 0
   assert account.account_number == 2
   assert account_2.name == "John"
   assert account_2.balance == 0
   assert account_2.account_number == 3