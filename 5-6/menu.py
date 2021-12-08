from collection import *
from validation import *
import  sys
from memento import *

def option_menu():
    print("1 - to see information\n"
          "2 - to add\n"
          "3 - to delete\n"
          "4 - to find\n"
          "5 - to replace\n"
          "6 - to sort\n"
          "7 - undo \n"
          "8 - redo \n"
          "9 - end work \n")


def main_menu():
    path = "text.txt"
    data = Collection(path)
    data.read()
    originator = Originator()
    caretaker = CareTaker()
    memento(originator, caretaker, data)
    while True:
        option_menu()
        option = input()
        if option == "9":
            sys.exit()
        if option == '1':
            print(data)
        elif option == '2':
            data.add()
            memento(originator, caretaker, data)
        elif option == '3':
            data.remove(int(input("Input ID:")))
            memento(originator, caretaker, data)
        elif option == '4':
            search_object = input("Input: ")
            data.search(search_object)
        elif option == '5':
            new_request = Vaccination_request()
            new_request.input()
            data.replace(new_request)
            memento(originator, caretaker, data)
        elif option == '6':
            print("Input parameter: \n(id, patient_name,patient_phone, vaccine, date, start_time, end_time)")
            parameter = myvalidate_vaccine([str(item) for item in Vaccination_request.__dict__], f"get_{input()}")
            print(data.sort(parameter))
        elif option == '7':
            originator.restore(caretaker.undo())
            write_changes_after(originator, path)
            data.read()
        elif option == '8':
            originator.restore(caretaker.redo())
            write_changes_after(originator, path)
            data.read()
        else:
            print("Incorrect. Try again!")


main_menu()