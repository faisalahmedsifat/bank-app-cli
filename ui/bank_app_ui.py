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
    def get_user_choice():
        return input("Enter your choice: ")
    
    @staticmethod
    def create_new_user():
        print("Creating a new user...")
        
    @staticmethod
    def display_all_accounts():
        print("Displaying all accounts...")
        
    @staticmethod
    def update_an_account():
        print("Updating an account...")
        
    @staticmethod
    def delete_an_account():
        print("Deleting an account...")
        
    @staticmethod
    def deposit_to_an_account():
        print("Depositing to an account...")
        
    @staticmethod
    def withdraw_from_an_account():
        print("Withdrawing from an account...")
        
    @staticmethod
    def search_for_an_account():
        print("Searching for an account...")
