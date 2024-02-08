from datetime import datetime
from insfrastructure.entities.bank_account_entity import BankAccountEntity
from insfrastructure.repositories.bank_account_repository import BankAccountRepository


class UpdateAccountUseCase:
    def __init__(self, bank_account_repo: BankAccountRepository):
        self.bank_account_repo = bank_account_repo

    def execute(self, bank_account_id: int, first_name: str, last_name: str, date_of_birth: datetime, email: str, national_id: str, phone_number: str, parmanent_address: str) -> bool:
        return self.bank_account_repo.update(bank_account_id, first_name, last_name, date_of_birth, email, national_id, phone_number, parmanent_address)