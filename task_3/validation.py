import datetime

def validate_id(id = None):
    if id == None:
        id = input()
    if isinstance(id, str):
        id = validate_numb(id)
        if id > 0:
            return id
        print('value must be positive!\n'
              'try again: ')
        return validate_id()

def validate_numb(numb = None):
    if numb == None:
        numb = input()
    try:
        n_numb = int(numb)
    except ValueError:
        print(numb,'value must be integer!\n'
              'try again: ')
        return validate_numb()
    return n_numb

def name_validation(name = None):
    if name == None:
        name = input()
    if not name.isalpha() :
        print(name, 'must consist of letters!\n'
              'try again: ')
        return name_validation()
    return name

def validate_phone(phone = None):
    if phone == None:
        phone = input()
    if isinstance(phone, str):
        code = '+'
        new_x = validate_numb(phone)
        if len(str(new_x)) != 12 or code not in str(phone):
            print(code + str(new_x),'wrong number! try again: ')
            return validate_phone()
        return code + str(new_x)
    return validate_phone()

def validate_vaccine(list, vaccine =None):
    if vaccine == None:
        vaccine = input()
    if vaccine not in list:
        print(vaccine,'we have not this vaccine!\n'
              'try again: ')
        return validate_vaccine(list)
    return vaccine

def validate_date(date = None):
    if date == None:
        date = input()
    if isinstance(date, str):
        try:
            return datetime.datetime.strptime(date, '%d/%m/%Y')
        except:
            print(date,'wrong format of date!\n'
                  'try again: ')
            return validate_date()
    return date

def validate_time(time = None):
    if time == None:
        time = input()
    if isinstance(time, str):
        try:
            return datetime.datetime.strptime(time, '%H:%M')
        except:
            print(time,'wrong format for time!\n'
                  'try again: ')
            return validate_time()
    return time

