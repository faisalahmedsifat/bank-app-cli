import { BankAccountRepository } from '../repositories/bank_account_repository';
import { BankAccountEntity } from '../entities/bank_account_entity';

export class GetAccountByIdUseCase {
    constructor(private bank_account_repo: BankAccountRepository) { }

    execute(account_id: number): BankAccountEntity | null {
        return this.bank_account_repo.find_by_id(account_id);
    }
}
