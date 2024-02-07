from abc import ABC, abstractmethod

from insfrastructure.entities.bank_account_entity import BankAccountEntity
from insfrastructure.entities.person_entity import PersonEntity
from insfrastructure.enums.account_types import AccountType


class BankAccountRepository(ABC):
    @abstractmethod
    def find_by_id(self, bank_account_id: int) -> BankAccountEntity:
        pass
    
    @abstractmethod
    def create(self, account_holder: PersonEntity, initial_deposit: float, account_type: AccountType) -> BankAccountEntity:
        pass
    
    @abstractmethod
    def show_all_accounts(self) -> list[BankAccountEntity]:
        pass
    
    @abstractmethod
    def update(self):
        pass
    
    @abstractmethod
    def delete(self, bank_account_id: int) -> bool:
        pass
    
    @abstractmethod
    def deposit(self, bank_account_id: int, amount: float) -> bool:
        pass
    
    @abstractmethod
    def withdraw(self):
        pass
    
    @abstractmethod
    def search(self):
        pass
    
    
    
    
    