import datetime
import validation

class Vaccination_request:
    def __init__(self, id_='4354', patient_name_ = 'Oleksa', patient_phone_ = '+380981234567',
                 vaccine_ = 'phizer', date_ = '12/12/2021', start_time_ = '12:21',
                 end_time_ = '15:12'):
        self.id = self.set_id(id_)
        self.patient_name = self.set_patient_name(patient_name_)
        self.patient_phone = self.set_patient_phone(patient_phone_)
        self.vaccine = self.set_vaccine(vaccine_)
        self.date = self.set_date(date_)
        self.start_time = self.set_start_time(start_time_)
        self.end_time = self.set_end_time(end_time_)

    @property
    def get_id(self):
        return self.id

    @property
    def get_patient_name(self):
        return self.patient_name

    @property
    def get_patient_phone(self):
        return self.patient_phone

    @property
    def get_vaccine(self):
        return self.vaccine

    @property
    def get_date(self):
        return self.date

    @property
    def get_start_time(self):
        return self.start_time

    @property
    def get_end_time(self):
        return self.end_time


    @validation.validate_numb
    @validation.validate_id
    def set_id(self, id):
        return id

    @validation.name_validation
    def set_patient_name(self, _patient_name):
        return _patient_name

    @validation.validate_phone
    def set_patient_phone(self, _patient_phone):
        return _patient_phone

    @validation.validate_vaccine(["phizer", "moderna", "astrazeneca"])
    def set_vaccine(self, _vaccine):
        return _vaccine

    @validation.validate_date
    def set_date(self, _date):
        return _date

    @validation.validate_time
    def set_start_time(self, _start_time):
        return _start_time

    @validation.validate_time
    def set_end_time(self, _end_time):
        return _end_time

    def __str__(self):
        return f"{self.id} {self.patient_name} {self.patient_phone} {self.vaccine} {self.date.strftime('%d/%m/%Y')} " + \
               f"{self.start_time.strftime('%H:%M')} {self.end_time.strftime('%H:%M')}"


    def input(self):
        setters = filter(lambda x: x.startswith('set'), list(Vaccination_request.__dict__.keys()))
        for item in setters:
            x = getattr(self, item)
            print(f"Input {x.__name__[4:]}: ")
            _input = input()
            x(_input)


    def is_found(self, search_object):
        all_parameters = (str(self)).split()
        for i in all_parameters:
            if str(search_object) in i:
                return True
        return False
