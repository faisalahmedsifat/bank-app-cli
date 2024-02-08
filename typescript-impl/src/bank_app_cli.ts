import { PersonEntity } from './infrastructure/entities/person_entity';
import { AccountType } from './infrastructure/enums/account_type';
import { Gender } from './infrastructure/enums/gender_choice';
import { BankAccountRepository } from './infrastructure/repositories/bank_account_repository';
import { CreateAccountUseCase } from './infrastructure/usecases/create_account_usecase';
import { DeleteAccountUseCase } from './infrastructure/usecases/delete_account_usecase';
import { DepositToAccountUseCase } from './infrastructure/usecases/deposit_usecase';
import { GetAccountByIdUseCase } from './infrastructure/usecases/get_account_by_id_usecase';
import { GetAllAccountsUseCase } from './infrastructure/usecases/get_all_accounts_usecase';
import { UpdateAccountUseCase } from './infrastructure/usecases/update_account_usecase';
import { WithdrawFromAccountUseCase } from './infrastructure/usecases/withdraw_from_account_usecase';
import { BankAppUI } from './ui/bank_app_ui';

// TODOS:
/*
ACCOUNT TYPES WE OFFER

*/

export class BankAppCLI {
    private ui: BankAppUI;
    private bank_account_repository: BankAccountRepository;
    private minimum_initial_deposit: Map<AccountType, number>;
    private minimum_balance_before_withdrawal: Map<AccountType, number>;

    constructor(ui: any, bank_account_repository: any) {
        this.ui = ui;
        this.bank_account_repository = bank_account_repository;
        this.minimum_initial_deposit = new Map([
            [AccountType.SAVINGS, 2000.0],
            [AccountType.CURRENT, 2000.0],
            [AccountType.FIXED, 5000.0],
            [AccountType.STUDENT, 500.0],
            [AccountType.SALARY, 1000.0],
            [AccountType.OTHERS, 6000.0],
        ]);

        this.minimum_balance_before_withdrawal = new Map([
            [AccountType.SAVINGS, 500.0],
            [AccountType.CURRENT, 500.0],
            [AccountType.FIXED, 2000.0],
            [AccountType.STUDENT, 0.0],
            [AccountType.SALARY, 500.0],
            [AccountType.OTHERS, 2000.0],
        ]);
    }

    public async create_new_account(): Promise<void> {
        // Get account holder details
        const first_name: any = await this.ui.get_user_input("Enter first name: ");
        const last_name: any = await this.ui.get_user_input("Enter last name: ");
        const date_of_birth: any= await this.ui.get_valid_date("Enter date of birth: ");
        const email: any = await this.ui.get_valid_email("Enter email: ");
        const national_id: any = await this.ui.get_user_input("Enter national id: ");
        const phone_number: any= await this.ui.get_user_input("Enter phone number: ");
        const parmanent_address: any= await this.ui.get_user_input("Enter permanent address: ");
        const gender: any= await this.ui.get_valid_gender("Enter gender: ");

        // Create account holder
        const account_holder: PersonEntity = new PersonEntity(
            first_name,
            last_name ,
            date_of_birth,
            email,
            gender, // Provide a default value for gender when it is null
            national_id,
            phone_number,
            parmanent_address
        );

        // Get account details
        var  account_type: any = await this.ui.get_valid_account_type("Enter account type: ", this.minimum_initial_deposit, this.minimum_balance_before_withdrawal);
        account_type = account_type ?? AccountType.SAVINGS; // Provide a default value for account_type when it is null 
        
        var initial_deposit: number | null = await this.ui.get_valid_amount("Enter initial deposit: ", this.minimum_initial_deposit, account_type);
        initial_deposit = initial_deposit ?? 0.0; // Provide a default value for initial_deposit when it is null
        const account: any = new CreateAccountUseCase(this.bank_account_repository).execute(account_holder, initial_deposit, account_type);

        // Show Account Details
        this.ui.show_account_details(account);
    }

    public display_all_accounts(): void {
        // Get All Accounts
        const accounts: any[] = new GetAllAccountsUseCase(this.bank_account_repository).execute();

        // Show All Accounts
        this.ui.display_all_accounts(accounts);
    }

    public async update_an_account(): Promise<void> {
        const account_number_to_be_updated: number | null = await this.ui.get_valid_account_id("Enter account number to update: ");
        if (!account_number_to_be_updated) {
            console.log("Account not found...");
            return;
        }
        const account: any = new GetAccountByIdUseCase(this.bank_account_repository).execute(account_number_to_be_updated);

        if (account) {
            console.log("Account found...\n");
            this.ui.show_account_details(account);
            console.log("\n");
            console.log("Enter new account holder details...\nPress \'Enter\' to skip updating an attribute...\n");

            const first_name: string | null = await this.ui.get_user_input(`Enter first name "${account.account_holder.first_name}": `, true);
            const updated_first_name: string = first_name ? first_name : account.account_holder.first_name;

            const last_name: string | null = await this.ui.get_user_input(`Enter last name "${account.account_holder.last_name}": `, true);
            const updated_last_name: string = last_name ? last_name : account.account_holder.last_name;

            const date_of_birth: Date | null = await this.ui.get_valid_date(`Enter date of birth "${account.account_holder.date_of_birth}": `, true);
            const updated_date_of_birth: Date = date_of_birth ? date_of_birth : account.account_holder.date_of_birth;

            const email: string | null = await this.ui.get_valid_email(`Enter email "${account.account_holder.email}": `, true);
            const updated_email: string = email ? email : account.account_holder.email;

            const national_id: string | null = await this.ui.get_user_input(`Enter national id "${account.account_holder.national_id}": `, true);
            const updated_national_id: string = national_id ? national_id : account.account_holder.national_id;

            const phone_number: string | null = await this.ui.get_user_input(`Enter phone number "${account.account_holder.phone_number}": `, true);
            const updated_phone_number: string = phone_number ? phone_number : account.account_holder.phone_number;

            const parmanent_address: string | null = await this.ui.get_user_input(`Enter permanent address "${account.account_holder.parmanent_address}": `, true);
            const updated_permanent_address: string = parmanent_address ? parmanent_address : account.account_holder.parmanent_address;

            const account_updated: boolean = new UpdateAccountUseCase(this.bank_account_repository).execute(account_number_to_be_updated, updated_first_name, updated_last_name, updated_date_of_birth, updated_email, updated_national_id, updated_phone_number, updated_permanent_address);
            if (account_updated) {
                console.log("Account updated successfully...\nupdated account details:");
                var acc: any = new GetAccountByIdUseCase(this.bank_account_repository).execute(account_number_to_be_updated);
                this.ui.show_account_details(acc);
            } else {
                console.log("Account not found...");
                return;
            }
        } else {
            console.log("Account not found...");
            return;
        }
    }

    public async delete_an_account(): Promise<void> {
        // Get account number to delete
        const account_number: number | null = await this.ui.get_valid_account_id("Enter account number to delete: ");
        if (!account_number) {
            console.log("Account not found...");
            return;
        }
        // Delete account
        const deleted: boolean = new DeleteAccountUseCase(this.bank_account_repository).execute(account_number);

        if (deleted) {
            console.log("Account deleted successfully...");
        } else {
            console.log("Account not found...");
        }
    }

    public async deposit_to_an_account(): Promise<void> {
        // Get account number and amount to deposit
        const account_number: number | null = await this.ui.get_valid_account_id("Enter account number to deposit to: ");
        const amount_to_be_deposit: number | null = await this.ui.get_valid_amount("Enter amount to deposit: ");

        if (!account_number || !amount_to_be_deposit) {
            console.log("Account not found...");
            return;
        }
        // Deposit to account
        const deposit_complete: boolean = new DepositToAccountUseCase(this.bank_account_repository).execute(account_number, amount_to_be_deposit);

        if (deposit_complete) {
            console.log(`Deposit complete succeeded of amount ${amount_to_be_deposit} to account number ${account_number}...\nupdated account details:`);
            var acc: any = new GetAccountByIdUseCase(this.bank_account_repository).execute(account_number);
            this.ui.show_account_details(acc);
        } else {
            console.log("Account not found...");
        }
    }

    public async withdraw_from_an_account(): Promise<void> {
        // Get account number and amount to withdraw
        const account_number: any = await this.ui.get_valid_account_id("Enter account number to withdraw from: ");
        const account: any = new GetAccountByIdUseCase(this.bank_account_repository).execute(account_number);
        if(!account) {
            console.log("Account not found...");
            return;
        }
        const amount_to_withdraw: any = await this.ui.get_valid_withdraw_amount("Enter amount to withdraw: ", this.minimum_balance_before_withdrawal, account);
        

        // Withdraw from account
        const withdrawal_complete: boolean = new WithdrawFromAccountUseCase(this.bank_account_repository).execute(account_number, amount_to_withdraw);
        if (withdrawal_complete) {
            console.log(`Withdrawal complete succeeded of amount ${amount_to_withdraw} from account number ${account_number}...\nupdated account details:`);
            this.ui.show_account_details(account);
        } else {
            console.log("Account not found...");
        }
    }

    public async search_for_an_account(): Promise<void> {
        // Get account number to search
        const account_number: any = await this.ui.get_valid_account_id("Enter account number to search: ");

        // Search for account
        const account: any = new GetAccountByIdUseCase(this.bank_account_repository).execute(account_number);

        if (account) {
            console.log("Account found...\n");
            this.ui.show_account_details(account);
        } else {
            console.log("Account not found...");
        }
    }

    public async loop(): Promise<void> {
        while (true) {
            this.ui.display_menu();
            const choice: any = await this.ui.get_user_input("Enter your choice: ");
            console.log("\n");

            switch (choice) {
                case "1":
                    await this.create_new_account();
                    break;
                case "2":
                    await this.display_all_accounts();
                    break;
                case "3":
                    await this.update_an_account();
                    break;
                case "4":
                    await this.delete_an_account();
                    break;
                case "5":
                    await this.deposit_to_an_account();
                    break;
                case "6":
                    await this.withdraw_from_an_account();
                    break;
                case "7":
                    await this.search_for_an_account();
                    break;
                case "8":
                    console.log("Exiting the program...");
                    return;
                default:
                    console.log("Invalid choice!!!");
            }

            console.log("\n");
        }
    }

    public run(): void {
        this.loop();
    }
}
