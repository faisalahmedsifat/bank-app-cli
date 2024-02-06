from insfrastructure.entities.person_entity import PersonEntity
from insfrastructure.usecases.create_account_usecase import CreateAccountUseCase
from repositories.bank_account_repository_impl import BankAccountRepositoryImpl
from ui.bank_app_ui import BankAppUI


class BankAppCLI:
    def __init__(self, ui, bank_account_repository):
        self.ui = ui
        self.bank_account_repository = bank_account_repository

    def create_new_account(self):
        
        # self.ui.create_new_account()
        first_name = self.ui.get_user_input("Enter first name: ")
        last_name = self.ui.get_user_input("Enter last name: ")
        gender = self.ui.get_user_input("Enter Gender: ")
        date_of_birth = self.ui.get_user_input("Enter date of birth: ")
        email = self.ui.get_user_input("Enter email: ")
        national_id = self.ui.get_user_input("Enter national id: ")
        phone_number = self.ui.get_user_input("Enter phone number: ")
        parmanent_address = self.ui.get_user_input("Enter permanent address: ")
        
        account_holder = PersonEntity(
                first_name=first_name, 
                last_name=last_name, 
                gender=gender, 
                date_of_birth=date_of_birth, 
                email=email, 
                national_id=national_id, 
                phone_number=phone_number, 
                parmanent_address=parmanent_address,
                )

        self.ui.show_user_details(account_holder)
        # self.ui.show_message("Account holder created successfully")
        initial_deposit = self.ui.get_user_input("Enter initial deposit: ")
        account = CreateAccountUseCase(self.bank_account_repository).execute(account_holder, initial_deposit)
        # self.ui.show_message(f"Account created successfully. Account number: {account.account_number}")
        self.ui.show_account_details(account)
        
        
        

    def display_all_accounts(self):
        # self.ui.display_all_accounts()
        # TODO
        pass 
    
    def update_an_account(self):
        # self.ui.update_an_account()
        # TODO
        pass

    def delete_an_account(self):
        # self.ui.delete_an_account()
        # TODO
        pass

    def deposit_to_an_account(self):
        # self.ui.deposit_to_an_account()
        # TODO
        pass

    def withdraw_from_an_account(self):
        # TODO
        pass

    def search_for_an_account(self):
        # TODO
        pass

    def loop(self):
        while True:
            ui.display_menu()
            choice = ui.get_user_input("Enter your choice: ")
            print("\n")

            if choice == "1":
                self.create_new_account()
            elif choice == "2":
                self.display_all_accounts()
            elif choice == "3":
                self.update_an_account()
            elif choice == "4":
                self.delete_an_account()
            elif choice == "5":
                self.deposit_to_an_account()
            elif choice == "6":
                self.withdraw_from_an_account()
            elif choice == "7":
                self.search_for_an_account()
            elif choice == "8":
                print("Exiting the program")
                break
            else:
                print("Invalid choice")
            print("\n")

    def run(self):
        self.loop()


if __name__ == "__main__":
    ui = BankAppUI()
    repository = BankAccountRepositoryImpl()
    app = BankAppCLI(ui, repository)
    app.run()