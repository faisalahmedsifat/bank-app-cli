import { Gender } from '../enums/gender_choice';
import { AccountType } from '../enums/account_type';

export class InputValidator {

    static validateGender(genderInput: string): Gender | null {
        try {
            const gender = Gender[genderInput.toUpperCase() as keyof typeof Gender];
            return gender || null; // Return null if the input string doesn't match any enum value
        } catch (error) {
            return null;
        }
    }

    static validateDate(dateStr: string): Date | null {
        try {
            const date = new Date(dateStr);
            if (isNaN(date.getTime())) {
                return null;
            }
            return date;
        } catch (error) {
            return null;
        }
    }

    static validateEmail(email: string): string | null {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (emailRegex.test(email)) {
            return email;
        } else {
            return null;
        }
    }

    static validateAmount(amount: string): number | null {
        try {
            const parsedAmount = parseFloat(amount);
            if (isNaN(parsedAmount)) {
                return null;
            }
            return parsedAmount;
        } catch (error) {
            return null;
        }
    }

    static validateWithdrawAmount(amount: string, minimumWithdrawAmount: any, accountBalance: number): number | null {
        try {
            const parsedAmount = parseFloat(amount);
            const amountAfterWithdrawal = accountBalance - parsedAmount;
            if (isNaN(parsedAmount) || amountAfterWithdrawal < minimumWithdrawAmount) {
                return null;
            }
            return parsedAmount;
        } catch (error) {
            return null;
        }
    }

    static validateAccountType(accountTypeInput: string): AccountType | null {
        try {
            const accountType = AccountType[accountTypeInput.toUpperCase() as keyof typeof AccountType];
            return accountType || null;
        } catch (error) {
            return null;
        }
    }

    static validateAccountId(accountId: string): number | null {
        try {
            const parsedAccountId = parseInt(accountId);
            if (isNaN(parsedAccountId)) {
                return null;
            }
            return parsedAccountId;
        } catch (error) {
            return null;
        }
    }
}
