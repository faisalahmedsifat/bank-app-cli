from insfrastructure.entities.bank_account_entity import BankAccountEntity
from insfrastructure.entities.person_entity import PersonEntity


class BankAppUI:

    def display_menu(self):
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

    def get_user_input(self, message: str = "Enter your choice: "):
        return input(message)
    
    def show_user_details(self, person: PersonEntity):
        print("Showing user details...")
        print()
        print(f"Name: {person.first_name} {person.last_name}")
        print(f"email: {person.email}")
        print(f"Phone: {person.phone_number}")
        print(f"National ID: {person.national_id}")
        print()
    
    def show_account_details(self, account: BankAccountEntity):
        print("Showing account details...")
        print()
        print(f"Account number: {account.account_number}")
        print(f"Account holder: {account.account_holder.first_name} {account.account_holder.last_name}")
        print(f"Balance: {account.balance}")
        print(f"Account type: {account.account_type}")
        print(f"Creation date: {account.creation_date}")
        print()