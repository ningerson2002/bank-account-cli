import sys
import getpass
from bank_account import BankAccount

BANK_NAME = "GENGAR BANK"
DATA = {}

def create_bank_account(name, password):
   """
   Create a new bank account and add its information to the database.

   Args:
      name: The name of the bank account holder.
      password: The password for the account.
   
   Returns:
      New bank account object.
   """
   DATA[name] = password
   return BankAccount(name)

def how_can_i_help(account):
   """
   Give the user access to account actions.

   Args:
      account: The account attached to the user.

   Returns:
      None.
   """
   print("How can we help you?")
   print("1. Deposit")
   print("2. Withdraw")
   print("3. Check your balance")
   print("4. Exit")
   decision = input("> ")
   if decision == "1":
      amount = int(input("Enter an amount to deposit: "))
      account.deposit(amount)
      how_can_i_help(account)
   elif decision == "2":
      amount = int(input("Enter an amount to withdraw: "))
      account.withdraw(amount)
      while amount > account.balance:
         amount = int(input("Enter a new amount: "))
         account.withdraw(amount)
      how_can_i_help(account)
   elif decision == "3":
      account.get_balance()
      how_can_i_help(account)
   else:
      print("Exiting...")
      sys.exit()

def main():
   print(f"Welcome to {BANK_NAME}", "! How can we help you?")
   print("1. Create a new account")
   print("2. Log into an existing account")
   print("3. Exit")
   decision = input("> ")
   if decision == "1":
      name = input("Enter your name: ")
      password = input("Enter your desired password: ")
      confirmation = input("Confirm your password: ")
      while confirmation != password:
         print("Passwords do not match.")
         password = input("Enter your desired password: ")
         confirmation = input("Confirm your password: ")
      account = create_bank_account(name, password)
      print(f"You may now log in as {name}")
      main()
   elif decision == "2":
      name = input("Enter your name: ")
      while name not in DATA.keys():
         print("Name not found. Please try again.")
         name = input("Enter your name: ")
      else:
         password = getpass.getpass("Enter your password: ")
         for i in DATA.keys():
            if name == i:
               while password != DATA.get(i):
                  password=getpass.getpass("Invalid password, please try again: ")
               break
         print("USER ID VERIFIED")
         account = BankAccount(name)
         print(account.welcome())
         how_can_i_help(account)
   elif decision == "3":
      print("Exiting...")
      sys.exit()
   else:
      print("Please enter a valid option.")
      main()
      
if __name__ == "__main__":
   main()