import sys
from collection import Collection
import validation
from vaccination_request import Vaccination_request

def option_menu():
    print("1 - to see information\n"
          "2 - to add\n"
          "3 - to delete\n"
          "4 - to find\n"
          "5 - to sort\n"
          "6 - to replace\n"
          "7 - to end work\n")

def main_menu():
    path = 'text.txt'
    data = Collection(path)
    data.read()
    option_menu()
    option = int(input())
    if option == 7:
        sys.exit()
    if option == 1:
        print(data)

    elif option == 2:
        data.add()
        print(data)
    elif option == 3:
        print("Input id:")
        id = input()
        data.remove(id)
        print(data)
    elif option == 4:
        print("Input:")
        search_object = input()
        data.search(search_object)
    elif option == 5:
        print("Input parameter: \n"
              "(id, patient_name,patient_phone, vaccine, date, start_time, end_time)")
        field = validation.myvalidate_vaccine([str(item) for item in Vaccination_request.__dict__], f"get_{input()}")
        data.sort(field)
    elif option == 6:
        data.replace()


    main_menu()