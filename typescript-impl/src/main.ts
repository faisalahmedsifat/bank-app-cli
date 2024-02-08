import { BankAppUI } from './ui/bank_app_ui';
import { BankAccountRepositoryImpl } from './repositories/bank_account_repository_impl';
import { BankAppCLI } from './bank_app_cli';

const ui = new BankAppUI();
const repository = new BankAccountRepositoryImpl();

const app = new BankAppCLI(ui, repository);
app.run();
