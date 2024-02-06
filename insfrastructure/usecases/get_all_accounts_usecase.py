from insfrastructure.entities.bank_account_entity import BankAccountEntity
from insfrastructure.repositories.bank_account_repository import BankAccountRepository


class GetAllAccountsUseCase:
    def __init__(self, bank_account_repo: BankAccountRepository):
        self.bank_account_repo = bank_account_repo

    def execute(self) -> list[BankAccountEntity]:
        return self.account_repository.show_all_accounts()