from insfrastructure.entities.person_entity import PersonEntity
from insfrastructure.enums.account_types import AccountType
from insfrastructure.repositories.bank_account_repository import BankAccountRepository


class CreateAccountUseCase:
    def __init__(self, bank_account_repo: BankAccountRepository):
        self.bank_account_repo = bank_account_repo

    def execute(self, account_holder: PersonEntity, initial_deposit: float, account_type: AccountType = AccountType.SAVINGS):
        return self.bank_account_repo.create(account_holder, initial_deposit, account_type)