import { BankAccountRepository } from '../repositories/bank_account_repository';

export class WithdrawFromAccountUseCase {
    constructor(private bank_account_repo: BankAccountRepository) { }

    execute(account_number: number, amount: number): boolean {
        return this.bank_account_repo.withdraw(account_number, amount);
    }
}
