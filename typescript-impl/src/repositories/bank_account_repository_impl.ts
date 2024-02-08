import { BankAccountRepository } from '../infrastructure/repositories/bank_account_repository';
import { BankAccountEntity } from '../infrastructure/entities/bank_account_entity';
import { PersonEntity } from '../infrastructure/entities/person_entity';
import { AccountType } from '../infrastructure/enums/account_type';

export class BankAccountRepositoryImpl implements BankAccountRepository {
    private bank_accounts: BankAccountEntity[];

    constructor() {
        this.bank_accounts = [];
    }

    find_by_id(bank_account_id: number): BankAccountEntity | null {
        const account = this.bank_accounts.find(account => account.account_number === bank_account_id);
        return account ? account : null;
    }

    create(account_holder: PersonEntity, initial_deposit: number, account_type: AccountType = AccountType.SAVINGS): BankAccountEntity {
        const account_number = this.bank_accounts.length + 1;
        const account = new BankAccountEntity(account_number, account_holder, initial_deposit, account_type);
        this.bank_accounts.push(account);
        return account;
    }

    show_all_accounts(): BankAccountEntity[] {
        return this.bank_accounts;
    }

    delete(bank_account_id: number): boolean {
        const index = this.bank_accounts.findIndex(account => account.account_number === bank_account_id);
        if (index !== -1) {
            this.bank_accounts.splice(index, 1);
            return true;
        }
        return false;
    }

    update(bank_account_id: number, first_name: string, last_name: string, date_of_birth: Date, email: string, national_id: string, phone_number: string, permanent_address: string): boolean {
        const account = this.find_by_id(bank_account_id);
        if (account) {
            account.account_holder.first_name = first_name;
            account.account_holder.last_name = last_name;
            account.account_holder.date_of_birth = date_of_birth;
            account.account_holder.email = email;
            account.account_holder.national_id = national_id;
            account.account_holder.phone_number = phone_number;
            account.account_holder.permanent_address = permanent_address;
            return true;
        }
        return false;
    }

    deposit(bank_account_id: number, amount: number): boolean {
        const account = this.find_by_id(bank_account_id);
        if (account) {
            account.balance += amount;
            return true;
        }
        return false;
    }

    withdraw(bank_account_id: number, amount: number): boolean {
        const account = this.find_by_id(bank_account_id);
        if (account && account.balance >= amount) {
            account.balance -= amount;
            return true;
        }
        return false;
    }
}
