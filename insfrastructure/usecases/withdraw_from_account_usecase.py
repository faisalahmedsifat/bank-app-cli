from insfrastructure.entities.person_entity import PersonEntity
from insfrastructure.enums.account_types import AccountType
from insfrastructure.repositories.bank_account_repository import BankAccountRepository


class WithdrawFromAccountUseCase:
    def __init__(self, bank_account_repo: BankAccountRepository):
        self.bank_account_repo = bank_account_repo

    def execute(self, account_number: int, amount: float) -> bool:
        return self.bank_account_repo.withdraw(account_number, amount)