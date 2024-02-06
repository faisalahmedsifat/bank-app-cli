from insfrastructure.repositories.bank_account_repository import BankAccountRepository


class DeleteAccountUseCase:
    def __init__(self, bank_account_repo: BankAccountRepository):
        self.bank_account_repo = bank_account_repo

    def execute(self, account_id: int) -> bool:
        return self.bank_account_repo.delete(account_id)
        