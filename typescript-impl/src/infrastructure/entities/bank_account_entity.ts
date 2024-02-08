import { v4 as uuidv4 } from 'uuid';
import { PersonEntity } from './person_entity';
import { AccountType } from '../enums/account_type';

export class BankAccountEntity {
    id: string;
    account_number: number;
    account_holder: PersonEntity;
    balance: number;
    account_type: AccountType;
    creation_date: Date;

    constructor(
        account_number: number,
        account_holder: PersonEntity,
        balance: number,
        account_type: AccountType,
        creation_date: Date | null = null,
    ) {
        this.id = uuidv4();
        this.account_number = account_number;
        this.account_holder = account_holder;
        this.balance = balance;
        this.account_type = account_type;
        this.creation_date = creation_date ? creation_date : new Date();
    }
}
