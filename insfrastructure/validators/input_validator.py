from datetime import datetime
import re
from insfrastructure.enums.gender_choice import Gender
from insfrastructure.enums.account_types import AccountType


class InputValidator:
    @staticmethod
    def validate_gender(gender_input):
        try:
            gender = Gender[gender_input.upper()]
            return gender
        except KeyError:
            return None

    @staticmethod
    def validate_date(date_str):
        try:
            date = datetime.strptime(date_str, "%Y-%m-%d")
            return date
        except ValueError:
            return None

    @staticmethod
    def validate_email(email):
        if re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return email
        else:
            return None

    @staticmethod
    def validate_amount(amount):
        try:
            amount = float(amount)
            return amount
        except ValueError:
            return None

    @staticmethod
    def validate_withdraw_amount(amount, minimum_withdraw_amount, account_balance):
        try:
            amount = float(amount)
            amount_after_withdrawal = account_balance - amount
            if amount_after_withdrawal < minimum_withdraw_amount:
                return None
            return amount
        except ValueError:
            return None

    @staticmethod
    def validate_account_type(account_type_input):
        try:
            account_type = AccountType[account_type_input.upper()]
            return account_type
        except KeyError:
            return None

    @staticmethod
    def validate_account_id(account_id):
        try:
            account_id = int(account_id)
            return account_id
        except ValueError:
            return None
