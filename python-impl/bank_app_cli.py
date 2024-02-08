
from insfrastructure.entities.person_entity import PersonEntity
from insfrastructure.enums.account_types import AccountType

from insfrastructure.usecases.create_account_usecase import CreateAccountUseCase
from insfrastructure.usecases.delete_account_usecase import DeleteAccountUseCase
from insfrastructure.usecases.deposit_usecase import DepositToAccountUseCase
from insfrastructure.usecases.get_account_by_id_usecase import GetAccountByIdUseCase
from insfrastructure.usecases.get_all_accounts_usecase import GetAllAccountsUseCase
from insfrastructure.usecases.update_account_usecase import UpdateAccountUseCase
from insfrastructure.usecases.withdraw_from_account_usecase import WithdrawFromAccountUseCase



class BankAppCLI:
    def __init__(self, ui, bank_account_repository):
        self.ui = ui
        self.bank_account_repository = bank_account_repository
        self.minimum_initial_deposit = {
            AccountType.SAVINGS: 2000.0,
            AccountType.CURRENT: 2000.0,
            AccountType.FIXED: 5000.0,
            AccountType.STUDENT: 500.0,
            AccountType.SALARY: 1000.0,
            AccountType.OTHERS: 6000.0,
        }
        
        self.minimum_balance_before_withdrawal = {
            AccountType.SAVINGS: 500.0,
            AccountType.CURRENT: 500.0,
            AccountType.FIXED: 2000.0,
            AccountType.STUDENT: 0.0,
            AccountType.SALARY: 500.0,
            AccountType.OTHERS: 2000.0,
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
        self.ui.display_all_accounts(accounts)
    
    def update_an_account(self):
        account_number_to_be_updated = self.ui.get_valid_account_id("Enter account number to update: ")
        account = GetAccountByIdUseCase(self.bank_account_repository).execute(account_number_to_be_updated)
        if account:
            print("Account found...\n")
            self.ui.show_account_details(account)
            print("\n")
            print("Enter new account holder details...\nPress \'Enter\' to skip updating an attribute...\n")
            
            first_name = self.ui.get_user_input(f"Enter first name \"{account.account_holder.first_name}\": ", returnNoneOnEmpty=True)
            if first_name == None: first_name = account.account_holder.first_name
            
            last_name = self.ui.get_user_input(f"Enter last name \"{account.account_holder.last_name}\": ", returnNoneOnEmpty=True)
            if last_name == None: last_name = account.account_holder.last_name
            
            date_of_birth = self.ui.get_valid_date(f"Enter date of birth \"{account.account_holder.date_of_birth}\": ", returnNoneOnEmpty=True)
            if date_of_birth == None: date_of_birth = account.account_holder.date_of_birth
            
            email = self.ui.get_valid_email(f"Enter email \"{account.account_holder.email}\": ", returnNoneOnEmpty=True)
            if email == None: email = account.account_holder.email
            
            national_id = self.ui.get_user_input(f"Enter national id \"{account.account_holder.national_id}\": ", returnNoneOnEmpty=True)
            if national_id == None: national_id = account.account_holder.national_id
            
            phone_number = self.ui.get_user_input(f"Enter phone number \"{account.account_holder.phone_number}\": ", returnNoneOnEmpty=True)
            if phone_number == None: phone_number = account.account_holder.phone_number
            
            parmanent_address = self.ui.get_user_input(f"Enter permanent address \"{account.account_holder.parmanent_address}\": ", returnNoneOnEmpty=True)
            if parmanent_address == None: parmanent_address = account.account_holder.parmanent_address
            
            account_updated = UpdateAccountUseCase(self.bank_account_repository).execute(account_number_to_be_updated, first_name, last_name, date_of_birth, email, national_id, phone_number, parmanent_address)
            if account_updated:
                print("Account updated successfully...\nupdated account details:")
                self.ui.show_account_details(GetAccountByIdUseCase(self.bank_account_repository).execute(account_number_to_be_updated))
            else:
                print("Account not found...")
                return
            
            
        else :
            print("Account not found...")
            return

    def delete_an_account(self):
        # Get account number to delete
        account_number = self.ui.get_valid_account_id("Enter account number to delete: ")

        # Delete account
        deleted = DeleteAccountUseCase(self.bank_account_repository).execute(account_number)

        if deleted:
            print("Account deleted successfully...")
        else:
            print("Account not found...") 


    def deposit_to_an_account(self):
        # Get account number and amount to deposit
        account_number = self.ui.get_valid_account_id("Enter account number to deposit to: ")
        amount_to_be_deposit = self.ui.get_valid_amount("Enter amount to deposit: ")

        # Deposit to account
        deposit_complete = DepositToAccountUseCase(self.bank_account_repository).execute(account_number, amount_to_be_deposit)

        if deposit_complete:
            print("Deposit complete succeeded of amount ", amount_to_be_deposit, " to account number ", account_number, "...\nupdated account details:")
            self.ui.show_account_details(GetAccountByIdUseCase(self.bank_account_repository).execute(account_number))
        else:
            print("Account not found...")
            
        

    def withdraw_from_an_account(self):
        # Get account number and amount to withdraw
        account_number = self.ui.get_valid_account_id("Enter account number to withdraw from: ")
        account = GetAccountByIdUseCase(self.bank_account_repository).execute(account_number)
        if(account == None):
            print("Account not found...")
            return
        amount_to_withdraw = self.ui.get_valid_withdraw_amount("Enter amount to withdraw: ", self.minimum_balance_before_withdrawal, GetAccountByIdUseCase(self.bank_account_repository).execute(account_number))

        # Withdraw from account
        withdrawal_complete = WithdrawFromAccountUseCase(self.bank_account_repository).execute(account_number, amount_to_withdraw)
        if withdrawal_complete:
            print("Withdrawal complete succeeded of amount ", amount_to_withdraw, " from account number ", account_number, "...\nupdated account details:")
            self.ui.show_account_details(GetAccountByIdUseCase(self.bank_account_repository).execute(account_number))
        else:
            print("Account not found...")
            
    def search_for_an_account(self):
        # Get account number to search
        account_number = self.ui.get_valid_account_id("Enter account number to search: ")
        
        # Search for account
        account = GetAccountByIdUseCase(self.bank_account_repository).execute(account_number)
        
        if account:
            print("Account found...\n")
            self.ui.show_account_details(account)
        else:
            print("Account not found...")

    def loop(self):
        while True:
            self.ui.display_menu()
            choice = self.ui.get_user_input("Enter your choice: ")
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
                print("Exiting the program...")
                break
            else:
                print()
                print("Invalid choice!!!")
                print()
            print("\n")
        
    def run(self):
        self.loop()
