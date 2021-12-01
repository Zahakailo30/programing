import datetime
import validation

class Vaccination_request:
    def __init__(self, id_='4354', patient_name_ = 'Oleksa', patient_phone_ = '+380981234567',
                 vaccine_ = 'phizer', date_ = datetime.date.today(), start_time_ = datetime.time(10,0),
                 end_time_ = datetime.time(12, 30)):
        self.id = validation.validate_id(id_)
        self.patient_name = validation.name_validation(patient_name_)
        self.patient_phone = validation.validate_phone(patient_phone_)
        self.vaccine = validation.validate_vaccine(['phizer', 'moderna', 'astrazeneca'], vaccine_)
        self.date = validation.validate_date(date_)
        self.start_time = validation.validate_time(start_time_)
        self.end_time = validation.validate_time(end_time_)

    @property
    def get_id(self):
        return self.id
    def get_patient_name(self):
        return self.patient_name
    def get_patient_phone(self):
        return self.patient_phone
    def get_vaccine(self):
        return self.vaccine
    def get_date(self):
        return self.date
    def get_start_time(self):
        return self.start_time
    def get_end_time(self):
        return self.end_time

    def __str__(self):
        return f"{self.id} {self.patient_name} {self.patient_phone} {self.vaccine} {self.date.strftime('%d/%m/%Y')} " + \
               f"{self.start_time.strftime('%H:%M')} {self.end_time.strftime('%H:%M')}"

    def input(self):
        print("id:")
        self.id = validation.validate_id()
        print("Patient name:")
        self.patient_name = validation.name_validation()
        print("Patient phone:")
        self.patient_phone = validation.validate_phone()
        print("Vaccine:")
        self.vaccine = validation.validate_vaccine(['phizer', 'moderna', 'astrazeneca'])
        print("Date:")
        self.date = validation.validate_date()
        print("Start time:")
        self.start_time = validation.validate_time()
        print("End time:")
        self.end_time = validation.validate_time()

    def is_found(self, search_object):
        all_parameters = (str(self)).split()
        for i in all_parameters:
            if str(search_object) in i:
                return True
        return False
