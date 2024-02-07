from insfrastructure.repositories.bank_account_repository import BankAccountRepository


class DepositToAccountUseCase:
    def __init__(self, bank_account_repo: BankAccountRepository):
        self.bank_account_repo = bank_account_repo

    def execute(self, account_id: int, amount: float) -> bool:
        return self.bank_account_repo.deposit(account_id, amount)
        