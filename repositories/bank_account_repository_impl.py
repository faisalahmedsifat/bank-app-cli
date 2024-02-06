from uuid import uuid4
from insfrastructure.entities.bank_account_entity import BankAccountEntity
from insfrastructure.entities.person_entity import PersonEntity
from insfrastructure.enums.account_types import AccountTypes
from insfrastructure.repositories.bank_account_repository import BankAccountRepository


class BankAccountRepositoryImpl(BankAccountRepository):
    def __init__(self):
        self.bank_accounts = []
        
    def find_by_id(self, bank_account_id: int):
        for account in self.bank_accounts:
            if account.id == bank_account_id:
                return account
        return None
    
    def create(self, account_holder: PersonEntity, initial_deposit: float, account_type: AccountTypes = AccountTypes.SAVINGS):
        account = BankAccountEntity(
            account_number=len(self.bank_accounts) + 1,
            account_holder=account_holder,
            balance=initial_deposit,
            account_type=account_type
        )
        self.bank_accounts.append(account)
        return account
    
    def show_all_accounts(self) -> list[BankAccountEntity]:
        return self.bank_accounts
    
    def delete(self, bank_account_id) -> bool:
        account = self.find_by_id(bank_account_id)
        if account:
            self.bank_accounts.remove(account)
            return True
        return False
    
    def update(self):
    #     account = self.find_by_id(bank_account_id)
    #     if account:
    #         account.account_holder = new_account_holder
            # return True
        return False
    
    def deposit(self):
        pass
    
    def withdraw(self):
        pass
    
    def search(self):
        pass
    
    
    
