import { BankAccountEntity } from '../entities/bank_account_entity';
import { PersonEntity } from '../entities/person_entity';
import { AccountType } from '../enums/account_type';

export interface BankAccountRepository {
    find_by_id(bank_account_id: number): BankAccountEntity;
    create(account_holder: PersonEntity, initial_deposit: number, account_type: AccountType): BankAccountEntity;
    show_all_accounts(): BankAccountEntity[];
    update(bank_account_id: number, first_name: string, last_name: string, date_of_birth: Date, email: string, national_id: string, phone_number: string, parmanent_address: string): void;
    delete(bank_account_id: number): boolean;
    deposit(bank_account_id: number, amount: number): boolean;
    withdraw(bank_account_id: number, amount: number): boolean;
}
