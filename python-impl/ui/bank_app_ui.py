from datetime import datetime
import re

from tabulate import tabulate
from insfrastructure.entities.bank_account_entity import BankAccountEntity
from insfrastructure.entities.person_entity import PersonEntity
from insfrastructure.enums.account_types import AccountType
from insfrastructure.enums.gender_choice import Gender
from insfrastructure.validators.input_validator import InputValidator


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
    def get_user_input( message: str = "Enter your choice: ", returnNoneOnEmpty: bool = False):
        while True:
            input_message = input(message)
            if not input_message.strip():
                if returnNoneOnEmpty: 
                    return None
                else:
                    continue
            return input_message
        
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
    def show_account_details(account: BankAccountEntity, details_text: bool = True):
        if details_text:
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
        for account_type in AccountType:
            data.append([account_type.name, minimum_initial_deposit[account_type], minimum_balance_before_withdrawal[account_type]])
        table = tabulate(data, headers=headers, tablefmt="pretty")
        print(table)

    @staticmethod
    def display_all_accounts(accounts):
        print("Displaying all accounts...\n")
        if not accounts:
            print("No accounts found.")
        for account in accounts:
            BankAppUI.show_account_details(account, details_text=False)

    @staticmethod
    def get_valid_gender(prompt, returnNoneOnEmpty: bool = False):
        while True:
            gender_input = BankAppUI.get_user_input(prompt, returnNoneOnEmpty=True)
            
            if gender_input is None:
                if returnNoneOnEmpty:
                    return None
            else:
                gender = InputValidator.validate_gender(gender_input)
                if gender is not None:
                    return gender
            
                print("Invalid gender choice. Please enter \"male\", \"female\", or \"other\".")

    @staticmethod
    def get_valid_date(prompt, returnNoneOnEmpty: bool = False):
        while True:
            date_str = BankAppUI.get_user_input(prompt, returnNoneOnEmpty=True)
            if date_str is None:
                if returnNoneOnEmpty:
                    return None
            else:
                date = InputValidator.validate_date(date_str)
                if date is not None:
                    return date
            print("Invalid date format. Please enter date in the format YYYY-MM-DD.")


    @staticmethod
    def get_valid_email(prompt, returnNoneOnEmpty: bool = False):
        while True:
            email = BankAppUI.get_user_input(prompt, returnNoneOnEmpty=True)
            if email is None:
                if returnNoneOnEmpty:
                    return None
            else:
                validated_email = InputValidator.validate_email(email)
                if validated_email is not None:
                    return validated_email
                print("Invalid email address format. Please enter a valid email address.")


    @staticmethod
    def get_valid_amount(prompt, minimum_amount=None, account_type=None, returnNoneOnEmpty: bool = False):
        while True:
            amount = BankAppUI.get_user_input(prompt, returnNoneOnEmpty=True)
            if amount is None:
                if returnNoneOnEmpty:
                    return None
            else:
                validated_amount = InputValidator.validate_amount(amount)
                if validated_amount is not None:
                    if minimum_amount and account_type:
                        if validated_amount < minimum_amount[account_type]:
                            print(f"Amount must be greater than {minimum_amount[account_type]} for {account_type.name} account. Please enter a valid amount.")
                            continue
                    return validated_amount
                print("Invalid amount. Please enter a valid amount.")
                


    @staticmethod
    def get_valid_withdraw_amount(prompt, minimum_withdraw_amount, account, returnNoneOnEmpty: bool = False):
        while True:
            amount = BankAppUI.get_user_input(prompt, returnNoneOnEmpty=True)
            if amount is None:
                if returnNoneOnEmpty:
                    return None
            else:
                validated_amount = InputValidator.validate_withdraw_amount(amount, minimum_withdraw_amount[account.account_type], account.balance if account else 0)
                if validated_amount is not None:
                    return validated_amount
                print(f"Invalid amount. Account must have {minimum_withdraw_amount[account.account_type]} for a {account.account_type.name} account after withdrawal. Please enter a valid amount.")


    @staticmethod
    def get_valid_account_type(prompt, minimum_initial_deposit, minimum_balance_before_withdrawal, returnNoneOnEmpty: bool = False):
        BankAppUI.show_account_types(minimum_initial_deposit=minimum_initial_deposit, minimum_balance_before_withdrawal=minimum_balance_before_withdrawal)
        while True:
            account_type_input = BankAppUI.get_user_input(prompt, returnNoneOnEmpty=True)
            if account_type_input is None:
                if returnNoneOnEmpty:
                    return None
            else:
                validated_account_type = InputValidator.validate_account_type(account_type_input)
                if validated_account_type is not None:
                    return validated_account_type
                print("Invalid account type. Please enter either one of the following: ")
                for account_type in AccountType:
                    print(account_type.name.lower())


    @staticmethod
    def get_valid_account_id(prompt, returnNoneOnEmpty: bool = False):
        while True:
            account_id = BankAppUI.get_user_input(prompt, returnNoneOnEmpty=True)
            if account_id is None:
                return None
            else:
                validated_account_id = InputValidator.validate_account_id(account_id)
                if validated_account_id is not None:
                    return validated_account_id
                print("Invalid account number. Please enter a valid account number.")
