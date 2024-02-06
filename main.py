
from insfrastructure.entities.person_entity import PersonEntity
from insfrastructure.enums.account_types import AccountTypes
from insfrastructure.usecases.create_account_usecase import CreateAccountUseCase
from insfrastructure.usecases.get_all_accounts_usecase import GetAllAccountsUseCase
from repositories.bank_account_repository_impl import BankAccountRepositoryImpl
from ui.bank_app_ui import BankAppUI


class BankAppCLI:
    def __init__(self, ui, bank_account_repository):
        self.ui = ui
        self.bank_account_repository = bank_account_repository
        self.minimum_initial_deposit = {
            AccountTypes.SAVINGS: 2000.0,
            AccountTypes.CURRENT: 2000.0,
            AccountTypes.FIXED: 5000.0,
            AccountTypes.STUDENT: 500.0,
            AccountTypes.SALARY: 1000.0,
            AccountTypes.OTHERS: 6000.0,
        }
        
        self.minimum_balance_before_withdrawal = {
            AccountTypes.SAVINGS: 500.0,
            AccountTypes.CURRENT: 500.0,
            AccountTypes.FIXED: 2000.0,
            AccountTypes.STUDENT: 0.0,
            AccountTypes.SALARY: 500.0,
            AccountTypes.OTHERS: 2000.0,
        }

    def create_new_account(self):
        
        # Get account holder details            
        first_name = self.ui.get_user_input("Enter first name: ")
        last_name = self.ui.get_user_input("Enter last name: ")
        date_of_birth = self.ui.get_valid_date("Enter date of birth: ")
        email = self.ui.get_valid_email("Enter email: ")
        national_id = self.ui.get_user_input("Enter national id: ")
        phone_number = self.ui.get_user_input("Enter phone number: ")
        parmanent_address = self.ui.get_user_input("Enter permanent address: ")
        gender = self.ui.get_valid_gender("Enter gender: ") 
       
        #  Create account holder 
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

        # Get account details
        account_type = self.ui.get_valid_account_type("Enter account type: ", self.minimum_initial_deposit, self.minimum_balance_before_withdrawal)

        initial_deposit = self.ui.get_valid_amount("Enter initial deposit: ", self.minimum_initial_deposit, account_type)
        account = CreateAccountUseCase(self.bank_account_repository).execute(account_holder, initial_deposit, account_type)
        
        # Show Account Details
        self.ui.show_account_details(account)
        

    def display_all_accounts(self):
        # Get All Accounts
        accounts = GetAllAccountsUseCase(self.bank_account_repository).execute()

        # Show All Accounts
        self.ui.show_all_accounts(accounts)
    
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