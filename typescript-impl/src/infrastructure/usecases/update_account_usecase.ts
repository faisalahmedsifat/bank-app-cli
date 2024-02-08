import { BankAccountRepository } from '../repositories/bank_account_repository';

export class UpdateAccountUseCase {
    private bank_account_repo: BankAccountRepository;

    constructor(bank_account_repo: BankAccountRepository) {
        this.bank_account_repo = bank_account_repo;
    }

    public execute(bank_account_id: number, first_name: string, last_name: string, date_of_birth: Date, email: string, national_id: string, phone_number: string, parmanent_address: string): boolean {
        return this.bank_account_repo.update(bank_account_id, first_name, last_name, date_of_birth, email, national_id, phone_number, parmanent_address);
    }
}
