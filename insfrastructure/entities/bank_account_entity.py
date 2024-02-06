from datetime import datetime
from insfrastructure.entities.person_entity import PersonEntity
from insfrastructure.enums.account_types import AccountTypes


class BankAccountEntity:
    def __init__(
            self, 
            id: int, 
            account_number: str, 
            account_holder: PersonEntity, 
            balance: float, 
            account_type: AccountTypes,
            creation_date:datetime = None,
            ):
        self.id = id
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
        self.account_type = account_type
        self.creation_date = creation_date if creation_date is not None else datetime.now()