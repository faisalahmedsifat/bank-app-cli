import { v4 as uuidv4 } from 'uuid';
import { Gender } from '../enums/gender_choice';

export class PersonEntity {
    id: string;
    first_name: string;
    last_name: string;
    date_of_birth: Date;
    gender: Gender;
    email: string;
    national_id: string;
    permanent_address: string;
    phone_number: string;

    constructor(
        first_name: string,
        last_name: string,
        date_of_birth: Date,
        email: string,
        gender: Gender,
        national_id: string,
        phone_number: string,
        permanent_address: string,
    ) {
        this.id = uuidv4();
        this.first_name = first_name;
        this.last_name = last_name;
        this.date_of_birth = date_of_birth;
        this.gender = gender;
        this.email = email;
        this.national_id = national_id;
        this.permanent_address = permanent_address;
        this.phone_number = phone_number;
    }
}
