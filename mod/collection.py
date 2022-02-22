from Flight_booking import FlightBooking
class Collection:
    def __init__(self, _file_name):
        self.req = []
        self.file_name = _file_name

    def add_req(self):
        new_req = FlightBooking()
        new_req.input()
        self.req.append(new_req)
        file = open(self.file_name, "w")
        for item in self.req:
            new_request = str(item) + "\n"
            file.write(new_request)
        file.close()
        return self

    def read_from_file(self):
        file = open(self.file_name, 'r')
        for i, line in enumerate(file):
            info = line.split()
            all_ = FlightBooking(*info)
            self.req.append(all_)
        file.close()
        return self
