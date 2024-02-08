import { BankAccountRepository } from '../repositories/bank_account_repository';
import { BankAccountEntity } from '../entities/bank_account_entity';

export class GetAllAccountsUseCase {
    constructor(private bank_account_repo: BankAccountRepository) { }

    execute(): BankAccountEntity[] {
        return this.bank_account_repo.show_all_accounts();
    }
}
