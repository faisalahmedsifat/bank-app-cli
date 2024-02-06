from uuid import uuid4

class PersonEntity:
    def __init__(
            self,
            # id: uuid4(), 
            first_name: str, 
            last_name: str, 
            date_of_birth: str, 
            email: str, 
            national_id: str, 
            phone_number: str = 'N/A', 
            parmanent_address: str = 'N/A', 
            gender: str = 'N/A',
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