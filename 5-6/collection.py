from vaccination_request import Vaccination_request

class Collection:
    def __init__(self, file_name = "text.txt"):
        self.requests = []
        self.file_name = file_name

    def __len__(self):
        return len(self.requests)

    def __str__(self):
        all_req = ""
        for item in self.requests:
            all_req += str(item) + "\n"
        return all_req

    def add(self, new_request = None):
        if new_request == None:
            new_request = Vaccination_request()
            new_request.input()
        self.requests.append(new_request)
        self.change_file()
        return self

    def change_file(self):
        file = open(self.file_name, 'w')
        for item in self.requests:
            file.write(str(item)+"\n")
        file.close()
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
                return True
        if flag == False:
            print ("there isn't any result")
            return False

    def replace(self,new_request):
        for item in self.requests:
            if item.is_found(new_request.get_id):
                self.requests.insert(self.requests.index(item),new_request)
                self.requests.remove(item)
                break
        self.change_file()
        return self

    def read(self):
        file = open(self.file_name, 'r')
        self.requests = []
        for i, line in enumerate(file):
            dani = line.split()
            request = Vaccination_request(*dani)
            self.requests.append(request)
        self.change_file()
        file.close()
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

    def set_requests(self,requests):
        self.requests = requests

    def get_requests(self):
        return self.requests

    def do_copy(self):
        cop = self.requests.copy()
        return cop

#def read_mistakes(path_to_file):
#    file = open(path_to_file,'r')
#    print(file.read())
#    file.close()
#    return