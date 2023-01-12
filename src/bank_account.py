class BankAccount:
   default_acc_number = 1

   def __init__(self, name, balance=0):
      self.name = name
      self.balance = balance
      self.account_number = BankAccount.default_acc_number
      BankAccount.default_acc_number += 1
   
   def welcome(self):
      print(f"Hi, {self.name}! Your account number is {self.account_number}, and you have {self.balance} available in your account.")

   def deposit(self, amount):
      print(f"Depositing {amount} to {self.name}'s account!")
      self.balance += amount
   
   def withdraw(self, amount):
      if self.balance < amount:
         print("Not enough funds to withdraw.")
      else:
         decision = input(f"Are you sure you want to withdraw {amount} from your account? (y/n): ")
         if decision == "y":
            print(f"Okay, withdrawing {amount} from {self.name}'s account!")
            self.balance -= amount
         else:
            print(f"Cancelled withdrawal of {amount} from {self.name}'s account.")

   def get_balance(self):
      print(f"You have {self.balance} in your account!")
