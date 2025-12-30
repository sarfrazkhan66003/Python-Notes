# Import necessary modules
import random

class Account:
    # Constructor to initialize account details
    def __init__(self, account_type, name, address, phone, aadhaar, pan, balance=0):
        self.account_type = account_type
        self.balance = balance
        self.transaction_count = 0
        self.transactions = []  # Stores transaction history for the mini statement
        # Customer details
        self.name = name
        self.address = address
        self.phone = phone
        self.aadhaar = aadhaar
        self.pan = pan

    # Deposit method
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Deposit: +{amount}")
            print(f"Successfully deposited {amount}. Current balance: {self.balance}")
        else:
            print("Invalid deposit amount.")

    # Withdraw method with validation for amount multiples and withdrawal limit
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        elif amount % 100 != 0:
            print("Please enter an amount in multiples of 100.")
        elif amount > 100000:
            print("Cannot withdraw more than 1 lakh in a single transaction.")
        else:
            self.balance -= amount
            self.transaction_count += 1
            self.transactions.append(f"Withdraw: -{amount}")
            print(f"Successfully withdrawn {amount}. Current balance: {self.balance}")
            # Apply penalty if more than 5 consecutive withdrawals
            if self.transaction_count > 5:
                penalty = 50  # Penalty amount
                self.balance -= penalty
                self.transactions.append(f"Penalty: -{penalty}")
                print(f"Penalty of {penalty} imposed. Current balance: {self.balance}")

    # View account information including personal details
    def view_account_info(self):
        print(f"Account Type: {self.account_type}")
        print(f"Balance: {self.balance}")
        print(f"Name: {self.name}")
        print(f"Address: {self.address}")
        print(f"Phone: {self.phone}")
        print(f"Aadhaar: {self.aadhaar}")
        print(f"PAN: {self.pan}")

    # View mini statement showing last few transactions
    def mini_statement(self):
        print("Mini Statement:")
        for transaction in self.transactions[-5:]:
            print(transaction)


class BankingSystem:
    def __init__(self):
        self.users = {}  # To store user data with account number as key

    # User validation to check if the account exists
    def validate_user(self, account_number):
        return account_number in self.users

    # Create account with initial details and prompt user for input
    def create_account(self):
        print("Creating a new account.")
        account_type = input("Enter account type (Saving/Current): ")
        name = input("Enter name: ")
        address = input("Enter address: ")
        phone = input("Enter phone number: ")
        aadhaar = input("Enter Aadhaar number: ")
        pan = input("Enter PAN number: ")
        
        # Generate a unique account number
        account_number = random.randint(10000, 99999)
        # Create an account object with customer details
        new_account = Account(account_type, name, address, phone, aadhaar, pan)
        # Add the new account to the users dictionary
        self.users[account_number] = new_account
        print(f"Account created successfully! Account Number: {account_number}")
        return account_number

    # Deposit functionality
    def deposit(self, account_number, amount):
        if self.validate_user(account_number):
            self.users[account_number].deposit(amount)
        else:
            print("Invalid account number.")

    # Withdraw functionality
    def withdraw(self, account_number, amount):
        if self.validate_user(account_number):
            self.users[account_number].withdraw(amount)
        else:
            print("Invalid account number.")

    # View account information
    def view_account_info(self, account_number):
        if self.validate_user(account_number):
            self.users[account_number].view_account_info()
        else:
            print("Invalid account number.")

    # View mini statement
    def mini_statement(self, account_number):
        if self.validate_user(account_number):
            self.users[account_number].mini_statement()
        else:
            print("Invalid account number.")


# Main program
banking_system = BankingSystem()

# Example usage with user inputs
# Step 1: Create a new account with user input for details
acc_number = banking_system.create_account()

# Step 2: Deposit money into the created account
deposit_amount = int(input("Enter amount to deposit: "))
banking_system.deposit(acc_number, deposit_amount)

# Step 3: Withdraw money from the account
withdraw_amount = int(input("Enter amount to withdraw: "))
banking_system.withdraw(acc_number, withdraw_amount)

# Step 4: View account information
banking_system.view_account_info(acc_number)

# Step 5: View mini statement
banking_system.mini_statement(acc_number)
