import { BankAccountRepository } from '../repositories/bank_account_repository';

export class DepositToAccountUseCase {
    constructor(private bank_account_repo: BankAccountRepository) { }

    execute(account_id: number, amount: number): boolean {
        return this.bank_account_repo.deposit(account_id, amount);
    }
}
