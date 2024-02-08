import { BankAccountEntity } from '../entities/bank_account_entity';
import { PersonEntity } from '../entities/person_entity';
import { AccountType } from '../enums/account_type';
import { BankAccountRepository } from '../repositories/bank_account_repository';

export class CreateAccountUseCase {
    constructor(private bank_account_repo: BankAccountRepository) { }

    execute(account_holder: PersonEntity, initial_deposit: number, account_type: AccountType = AccountType.SAVINGS): BankAccountEntity {
        return this.bank_account_repo.create(account_holder, initial_deposit, account_type);
    }
}
