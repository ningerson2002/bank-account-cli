"""
Manage a user bank account.
"""

class BankAccount:
   default_acc_number = 1

   def __init__(self, name, balance=0):
      """
      Create a new bank account with given parameters.

      Args:
         name: Name of the account holder.
         balance: Balance of the account. Default is 0.

      Returns:
         None.
      """
      self.name = name
      self.balance = balance
      self.account_number = BankAccount.default_acc_number
      BankAccount.default_acc_number += 1
   
   def welcome(self):
      """
      Welcome statement after a successful login.
      """
      print(f"Hi, {self.name}! Your account number is {self.account_number}, and you have ${self.balance} available in your account.")

   def deposit(self, amount):
      """
      Deposit a given amount to the account.
      
      Args:
         amount: Amount to deposit.

      Returns:
         None. Only adds deposited amount to account balance.
      """
      print(f"Depositing {amount} to {self.name}'s account!")
      self.balance += amount
   
   def withdraw(self, amount):
      """
      Withdraw a given amount from the account.

      Args:
         amount: Amount to withdraw.
      
      Returns:
         None. Only subtracts withraw amount to account balance.
      """
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
      """
      Gets the balance of the account.

      Args:
         None

      Returns:
         None
      """
      print(f"You have {self.balance} in your account!")
