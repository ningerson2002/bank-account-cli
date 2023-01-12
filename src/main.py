from bank_account import BankAccount

EXISTING_ACCOUNTS = []

def create_bank_account(name):
   EXISTING_ACCOUNTS.append(name)
   return BankAccount(name)

def does_account_exist(name):
   return name in EXISTING_ACCOUNTS

def main():
   print("Welcome to Gengar Bank! What can I help you with today?")
   print("1. Create a new account")
   print("2. Login to an existing account")
   print("3. Exit")
   decision = input("> ")