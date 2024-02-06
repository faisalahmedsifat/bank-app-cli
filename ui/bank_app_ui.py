from datetime import datetime
import re

from tabulate import tabulate
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
        print("Showing account details...\n")
        headers = ["Attribute", "Value"]
        data = [
            ["Name", f"{person.first_name} {person.last_name}"],
            ["Account holder's email", person.email],
            ["Account holder's phone number", person.phone_number],
            ["Account holder's national ID", person.national_id],
            ["Account holder's date of birth", person.date_of_birth],
            ["Account holder's gender", person.gender],
            ["Account holder's permanent address", person.parmanent_address]
            
        ]
        table = tabulate(data, headers=headers, tablefmt="pretty")
        print(table)
    
    @staticmethod
    def show_account_details(account: BankAccountEntity):
        print("Showing account details...\n")
        headers = ["Attribute", "Value"]
        data = [
            ["Account number", account.account_number],
            ["Account holder's name", f"{account.account_holder.first_name} {account.account_holder.last_name}"],
            ["Balance", account.balance],
            ["Account type", account.account_type],
            ["Creation date", account.creation_date],
            ["Account holder's email", account.account_holder.email],
            ["Account holder's phone number", account.account_holder.phone_number],
            ["Account holder's national ID", account.account_holder.national_id],
            ["Account holder's date of birth", account.account_holder.date_of_birth],
            ["Account holder's gender", account.account_holder.gender],
            ["Account holder's permanent address", account.account_holder.parmanent_address]
            
        ]
        table = tabulate(data, headers=headers, tablefmt="pretty")
        print(table)
    
    @staticmethod
    def show_account_types(minimum_initial_deposit, minimum_balance_before_withdrawal):
        print("Account types we offer...")
        headers = ["Account Type", "Minimum Initial Deposit", "Minimum Balance Before Withdrawal"]
        data = []
        for account_type in AccountTypes:
            data.append([account_type.name, minimum_initial_deposit[account_type], minimum_balance_before_withdrawal[account_type]])
        table = tabulate(data, headers=headers, tablefmt="pretty")
        print(table)


    
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
    def get_valid_amount(prompt, minimum_amount, account_type):
        while True:
            amount = BankAppUI.get_user_input(prompt)
            try:
                amount = float(amount)
                if(amount < minimum_amount[account_type]):
                    print(f"Amount must be greater than {minimum_amount[account_type]} for {account_type.name} account. Please enter a valid amount.")
                    continue
                return amount
            except ValueError:
                print("Invalid amount. Please enter a valid amount.")
                continue
            
    @staticmethod
    def get_valid_account_type(prompt, minimum_initial_deposit, minimum_balance_before_withdrawal):
        BankAppUI.show_account_types(minimum_initial_deposit=minimum_initial_deposit, minimum_balance_before_withdrawal=minimum_balance_before_withdrawal)
        while True:
            account_type_input = BankAppUI.get_user_input(prompt)
            try:
                account_type = AccountTypes[account_type_input.upper()]
                return account_type
            except KeyError:
                print("Invalid account type. Please enter either one of the following: ")
                for account_type in AccountTypes:
                    print(account_type.name.lower())
                    
                    
    @staticmethod
    def display_all_accounts(accounts):
        for account in accounts:
            BankAppUI.show_account_details(account)