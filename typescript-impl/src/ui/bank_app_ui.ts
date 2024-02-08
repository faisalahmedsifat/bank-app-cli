import { InputValidator } from '../infrastructure/validators/input_validator'; // Import the InputValidator class from its file
import { BankAccountEntity } from '../infrastructure/entities/bank_account_entity'; // Import the BankAccountEntity class from its file
import { PersonEntity } from '../infrastructure/entities/person_entity'; // Import the PersonEntity class from its file
import { AccountType } from '../infrastructure/enums/account_type'; // Import the AccountType enum from its file
import { Gender } from '../infrastructure/enums/gender_choice';
import { table } from 'console';

const readline = require('readline');

export class BankAppUI {
    display_menu(): void {
        const singleDashes: string = "-".repeat(50);
        const doubleDashes: string = "=".repeat(50);
        console.log("\n");
        console.log(doubleDashes);
        console.log("\tWelcome to the Bank App CLI");
        console.log(singleDashes);
        console.log("\nPlease select an option from the menu below");

        console.log("\n");
        console.log("1. Create a new account");
        console.log("2. Display all accounts");
        console.log("3. Update an account");
        console.log("4. Delete an account");
        console.log("5. Deposit an amount into your account");
        console.log("6. Withdraw an amount from your account");
        console.log("7. Search for account");
        console.log("8. Exit");
        console.log("\n");
    }

    async get_user_input(message: string = "Enter your choice: ", returnNoneOnEmpty: boolean = false): Promise<string | null> {
        while (true) {
            const inputMessage: string | null = await this.prompt_user(message) || "";
            if (inputMessage.length === 0) { // Check if the input string is empty
                if (returnNoneOnEmpty) {
                    return null;
                } else {
                    continue;
                }
            }
            return inputMessage;
        }
    }

    private prompt_user(message: string) {
        const rl = readline.createInterface({
            input: process.stdin,
            output: process.stdout
        });

        return new Promise<string>((resolve) => {
            rl.question(message, (input: string) => {
                rl.close();
                resolve(input);
            });
        });
    }

    show_user_details(person: PersonEntity): void {
        console.log("Showing account details...\n");
        const headers: string[] = ["Attribute", "Value"];
        const data: any[][] = [
            ["Name", `${person.first_name} ${person.last_name}`],
            ["Account holder's email", person.email],
            ["Account holder's phone number", person.phone_number],
            ["Account holder's national ID", person.national_id],
            ["Account holder's date of birth", person.date_of_birth],
            ["Account holder's gender", person.gender],
            ["Account holder's permanent address", person.permanent_address]
        ];
        // const table: string = this.formatTable(data, headers);
        // console.log(table(data));
        this.formatTable(data);
    }

    show_account_details(account: BankAccountEntity, detailsText: boolean = true): void {
        if (detailsText) {
            console.log("Showing account details...\n");
        }
        const headers: string[] = ["Attribute", "Value"];
        const data: any[][] = [
            ["Account number", account.account_number],
            ["Account holder's name", `${account.account_holder.first_name} ${account.account_holder.last_name}`],
            ["Balance", account.balance],
            ["Account type", account.account_type],
            ["Creation date", account.creation_date],
            ["Account holder's email", account.account_holder.email],
            ["Account holder's phone number", account.account_holder.phone_number],
            ["Account holder's national ID", account.account_holder.national_id],
            ["Account holder's date of birth", account.account_holder.date_of_birth],
            ["Account holder's gender", account.account_holder.gender],
            ["Account holder's permanent address", account.account_holder.permanent_address]
        ];
        // const table: string = this.formatTable(data, headers);
        // console.log(table(data));
        this.formatTable(data);
    }

    show_account_types(minimumInitialDeposit: Map<AccountType, number>, minimumBalanceBeforeWithdrawal: Map<AccountType, number>): void {
        console.log("Account types we offer...");
        const headers: string[] = ["Account Type", "Minimum Initial Deposit", "Minimum Balance Before Withdrawal"];
        const data: any[][] = [];
        for (const [accountType, initialDeposit] of minimumInitialDeposit.entries()) {
            data.push([accountType, initialDeposit, minimumBalanceBeforeWithdrawal.get(accountType)]);
        }
        // const table: string = this.formatTable(data, headers);
        // console.log(table(data));
        // table(data);
        this.formatTable(data);
    }

    display_all_accounts(accounts: BankAccountEntity[]): void {
        console.log("Displaying all accounts...\n");
        if (!accounts.length) {
            console.log("No accounts found.");
        }
        for (const account of accounts) {
            this.show_account_details(account, false);
        }
    }

    async get_valid_gender(prompt: string, returnNoneOnEmpty: boolean = false): Promise<Gender | null> {
        while (true) {
            const genderInput: string | null =await this.get_user_input(prompt, returnNoneOnEmpty);
            if (genderInput === null) {
                return null;
            }
            const gender: Gender | null = InputValidator.validateGender(genderInput);
            if (gender !== null) {
                return gender;
            }
            console.log("Invalid gender choice. Please enter \"male\", \"female\", or \"other\".");
        }
    }

    async get_valid_date(prompt: string, returnNoneOnEmpty: boolean = false): Promise<Date | null> {
        while (true) {
            const dateStr: string | null =await this.get_user_input(prompt, returnNoneOnEmpty);
            if (dateStr === null) {
                return null;
            }
            const date: Date | null = InputValidator.validateDate(dateStr);
            if (date !== null) {
                return date;
            }
            console.log("Invalid date format. Please enter date in the format YYYY-MM-DD.");
        }
    }

    async get_valid_email(prompt: string, returnNoneOnEmpty: boolean = false): Promise<string | null> {
        while (true) {
            const email: string | null =await this.get_user_input(prompt, returnNoneOnEmpty);
            if (email === null) {
                return null;
            }
            const validatedEmail: string | null = InputValidator.validateEmail(email);
            if (validatedEmail !== null) {
                return validatedEmail;
            }
            console.log("Invalid email address format. Please enter a valid email address.");
        }
    }

    async get_valid_amount(prompt: string, minimumAmount?: Map<AccountType, number>, accountType?: AccountType, returnNoneOnEmpty: boolean = false): Promise<number | null> {
        while (true) {
            const amount: string | null =await this.get_user_input(prompt, returnNoneOnEmpty);
            if (amount === null) {
                return null;
            }
            const validatedAmount: number | null = InputValidator.validateAmount(amount);
            if (validatedAmount !== null) {
                if (minimumAmount && accountType) {
                    if (validatedAmount < (minimumAmount.get(accountType) || 0)) {
                        console.log(`Amount must be greater than ${minimumAmount.get(accountType)} for ${accountType} account. Please enter a valid amount.`);
                        continue;
                    }
                }
                return validatedAmount;
            }
            console.log("Invalid amount. Please enter a valid amount.");
        }
    }

    async get_valid_withdraw_amount(prompt: string, minimumWithdrawAmount: Map<AccountType, number>, account: BankAccountEntity, returnNoneOnEmpty: boolean = false): Promise<number | null> {
        while (true) {
            const amount: string | null =await this.get_user_input(prompt, returnNoneOnEmpty);
            if (amount === null) {
                return null;
            }
            const validatedAmount: number | null = InputValidator.validateWithdrawAmount(amount, minimumWithdrawAmount.get(account.account_type) || 0, account.balance || 0);
            if (validatedAmount !== null) {
                return validatedAmount;
            }
            console.log(`Invalid amount. Account must have ${minimumWithdrawAmount} for a ${account.account_type} account after withdrawal. Please enter a valid amount.`);
        }
    }

    async get_valid_account_type(prompt: string, minimumInitialDeposit: Map<AccountType, number>, minimumBalanceBeforeWithdrawal: Map<AccountType, number>, returnNoneOnEmpty: boolean = false): Promise<AccountType | null> {
        this.show_account_types(minimumInitialDeposit, minimumBalanceBeforeWithdrawal);
        while (true) {
            const accountTypeInput: string | null =await this.get_user_input(prompt, returnNoneOnEmpty);
            if (accountTypeInput === null) {
                return null;
            }
            const validatedAccountType: AccountType | null = InputValidator.validateAccountType(accountTypeInput);
            if (validatedAccountType !== null) {
                return validatedAccountType;
            }
            console.log("Invalid account type. Please enter either one of the following: ");

            for (const accountType in AccountType) {
                console.log(accountType);
            }
        }
    }

    async get_valid_account_id(prompt: string, returnNoneOnEmpty: boolean = false): Promise<number | null> {
        while (true) {
            const accountId: string | null =await this.get_user_input(prompt, returnNoneOnEmpty);
            if (accountId === null) {
                return null;
            }
            const validatedAccountId: number | null = InputValidator.validateAccountId(accountId);
            if (validatedAccountId !== null) {
                return validatedAccountId;
            }
            console.log("Invalid account number. Please enter a valid account number.");
        }
    }

    private formatTable(data: any[][]): void {
        table(data);
    }
}
