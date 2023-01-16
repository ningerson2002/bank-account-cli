from colorama import Fore
import sys
from bank_account import BankAccount

BANK_NAME = Fore.MAGENTA + "GENGAR BANK"
EXISTING_ACCOUNTS = []

def create_bank_account(name):
   EXISTING_ACCOUNTS.append(name)
   return BankAccount(name)

# def does_account_exist(name):
#    return name in EXISTING_ACCOUNTS

def main():
   print(f"Welcome to {BANK_NAME}", "! How can we help you?")
   print("1. Create a new account")
   print("2. Log into an existing account")
   print("3. Exit")
   decision = input("> ")
   if decision == "1":
      name = input("Enter your name: ")
      account = create_bank_account(name)
      print(f"You may now log in as {name}")
      main()
   elif decision == "2":
      name = input("Enter your name: ")
      if name in EXISTING_ACCOUNTS:
         account = BankAccount(name)
         print(account.welcome())
         print("How can we help you?")
         print("1. Deposit")
         print("2. Withdraw")
         print("3. Check your balance")
         decision_2 = input("> ")
         if decision_2 == "1":
            amount = int(input("Enter an amount to deposit: "))
            account.deposit(amount)
            main()
         elif decision_2 == "2":
            amount = int(input("Enter an amount to withdraw: "))
            account.withdraw(amount)
            main()
         else:
            account.get_balance()
            main()
      else:
         print("Name not connected to an account.")
         main()
   elif decision == "3":
      print("Exiting...")
      sys.exit()
   else:
      print("Please enter a valid option.")
      main()
      
if __name__ == "__main__":
   main()