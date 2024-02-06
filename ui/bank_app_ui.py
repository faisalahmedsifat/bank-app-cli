from datetime import datetime
import re
from insfrastructure.entities.bank_account_entity import BankAccountEntity
from insfrastructure.entities.person_entity import PersonEntity
from insfrastructure.enums.account_types import AccountTypes
from insfrastructure.enums.gender_choice import Gender


class BankAppUI:
    @staticmethod
    def display_menu():
        single_dashes = "-" * 50
        double_dashes = "=" * 50
        print("\n")
        print(double_dashes)
        print("\tWelcome to the Bank App CLI")
        print(single_dashes)
        print("\nPlease select an option from the menu below")

        print("\n")
        print("1. Create a new account")
        print("2. Display all accounts")
        print("3. Update an account")
        print("4. Delete an account")
        print("5. Deposit an amount into your account")
        print("6. Withdraw an amount from your account")
        print("7. Search for account")
        print("8. Exit")
        print("\n")

    @staticmethod
    def get_user_input( message: str = "Enter your choice: "):
        return input(message)
    
    @staticmethod
    def show_user_details( person: PersonEntity):
        print("Showing user details...")
        print()
        print(f"Name: {person.first_name} {person.last_name}")
        print(f"email: {person.email}")
        print(f"Phone: {person.phone_number}")
        print(f"National ID: {person.national_id}")
        print(f"Date of birth: {person.date_of_birth}")
        print(f"Gender: {person.gender}")
        print()
    
    @staticmethod
    def show_account_details(account: BankAccountEntity):
        print("Showing account details...")
        print()
        print(f"Account number: {account.account_number}")
        print(f"Account holder: {account.account_holder.first_name} {account.account_holder.last_name}")
        print(f"Balance: {account.balance}")
        print(f"Account type: {account.account_type}")
        print(f"Creation date: {account.creation_date}")
        print()
    
    @staticmethod
    def get_valid_gender(prompt):
        while True:
            gender_input = BankAppUI.get_user_input(prompt)
            try:
                gender = Gender[gender_input.upper()]
                return gender
            except KeyError:
                print("Invalid gender choice, please write \"male\" or \"female\" or \"other\"")

    @staticmethod
    def get_valid_date(prompt):
        while True:
            date_str = BankAppUI.get_user_input(prompt)
            try:
                date = datetime.strptime(date_str, "%Y-%m-%d")
                return date
            except ValueError:
                print("Invalid date format. Please enter date in the format YYYY-MM-DD.")
                continue
            
    @staticmethod
    def get_valid_email(prompt):
        while True:
            email = BankAppUI.get_user_input(prompt)
            if re.match(r"[^@]+@[^@]+\.[^@]+", email):
                return email
            else:
                print("Invalid email address format. Please enter a valid email address.")
                
    @staticmethod
    def get_valid_amount(prompt):
        while True:
            amount = BankAppUI.get_user_input(prompt)
            try:
                amount = float(amount)
                return amount
            except ValueError:
                print("Invalid amount. Please enter a valid amount.")
                continue
            
    @staticmethod
    def get_valid_account_type(prompt):
        while True:
            account_type_input = BankAppUI.get_user_input(prompt)
            try:
                account_type = AccountTypes[account_type_input.upper()]
                return account_type
            except KeyError:
                print("Invalid account type. Please enter either one of the following: ")
                for account_type in AccountTypes:
                    print(account_type.name)
                    
                    
    @staticmethod
    def display_all_accounts(accounts):
        for account in accounts:
            BankAppUI.show_account_details(account)