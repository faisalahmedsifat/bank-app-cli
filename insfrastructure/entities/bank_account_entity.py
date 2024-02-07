from datetime import datetime
from uuid import UUID, uuid4
from insfrastructure.entities.person_entity import PersonEntity
from insfrastructure.enums.account_types import AccountType


class BankAccountEntity:
    def __init__(
            self, 
            account_number: int, 
            account_holder: PersonEntity, 
            balance: float, 
            account_type: AccountType,
            creation_date:datetime = None,
            ):
        self.id = uuid4()
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
        self.account_type = account_type
        self.creation_date = creation_date if creation_date is not None else datetime.now()