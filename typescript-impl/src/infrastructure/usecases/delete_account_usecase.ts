import { BankAccountRepository } from '../repositories/bank_account_repository';

export class DeleteAccountUseCase {
    constructor(private bank_account_repo: BankAccountRepository) { }

    execute(account_id: number): boolean {
        return this.bank_account_repo.delete(account_id);
    }
}
