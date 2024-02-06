from datetime import datetime
from uuid import uuid4

from insfrastructure.enums.gender_choice import Gender

class PersonEntity:
    def __init__(
            self,
            first_name: str, 
            last_name: str, 
            date_of_birth: datetime, 
            email: str, 
            gender: Gender,
            national_id: str, 
            phone_number: str, 
            parmanent_address: str, 
        ):
        self.id = uuid4()
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.email = email
        self.national_id = national_id
        self.parmanent_address = parmanent_address
        self.phone_number = phone_number