from bank_app_cli import BankAppCLI
from repositories.bank_account_repository_impl import BankAccountRepositoryImpl
from ui.bank_app_ui import BankAppUI

if __name__ == "__main__":
    ui = BankAppUI()
    repository = BankAccountRepositoryImpl()
    app = BankAppCLI(ui, repository)
    app.run()