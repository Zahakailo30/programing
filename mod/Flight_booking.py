#from collection import Time
from validation import *

class Time:
    def __init__(self, hour=0, minute=0):
        self.hour = hour
        self.minute = minute

class FlightBooking:
    time_list = [ ]
   # def add_time(self,time):
   #    self.time_list.append(time)

    def __init__(self, Avia_company , NoOfPeople,  Data, FlightNumber, StartTime = Time() , EndTime = Time() ):
        self.Avia_company = Avia_company
        self.NoOfPeople = NoOfPeople
        self.Startime = StartTime
        self.EndTime = EndTime
        self.Data = Data
        self.FlightNumber = FlightNumber

    def get_Avia_C(self):
        return self.Avia_company

    def get_NoOfPeople(self):
        return self.NoOfPeople

    def get_Start_Time(self):
        return self.Startime

    def get_End_Time(self):
        return self.EndTime
    def get_Data(self):
        return self.Data
    def get_FlightNumber(self):
        return self.FlightNumber
