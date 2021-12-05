import validation
from vaccination_request import Vaccination_request
from os.path import exists
import sys
class Collection:
    def __init__(self, file_name):
        self.requests = []
        self.file_name = file_name

    def __str__(self):
        all_req = ""
        for item in self.requests:
            all_req += str(item) + "\n"
        return all_req

    def read(self):
        if exists(self.file_name):
            file = open(self.file_name, 'r')
            for i, line in enumerate(file):
                dani = line.split()
                request = Vaccination_request(*dani)
                self.requests.append(request)
            self.change_file()
            file.close()
            return self
        else:
            print(f'{self.file_name} does not exists')
            sys.exit()

    def change_file(self):
        file = open(self.file_name, 'w')
        for item in self.requests:
            file.write(str(item)+"\n")
        return self

    def add(self):
        new_request = Vaccination_request()
        new_request.input()
        self.requests.append(new_request)
        self.change_file()
        return self

    def remove(self, id):
        for i in range(len(self.requests)):
            if str(self.requests[i].get_id) == str(id):
                self.requests.pop(i)
                break
        self.change_file()

    def search(self, x):
        flag = False
        for i in self.requests:
            if i.is_found(x):
                print(i)
                flag = True
        if flag == False:
            print ("there isn't any result")

    def replace(self):
        new_request = Vaccination_request()
        new_request.input()
        for item in self.requests:
            if item.is_found(new_request.get_id):
                self.requests.insert(self.requests.index(item), new_request)
                self.requests.remove(item)
                break
        self.change_file()
        return self

    def sort(self, parameter):
        parameters = self.requests[0].__dict__
        parameter = parameter.replace("get_", "")
        if parameter in parameters:
            self.requests.sort(key=lambda request_: getattr(request_, parameter))
        else:
            print('Wrong field')
            return
        for item in self.requests:
            self.change_file()
            print(item)
        return


def read_mistakes(path_to_file):
    file = open(path_to_file,'r')
    print(file.read())
    file.close()
    return