import datetime
from functools import wraps

def myvalidate_vaccine(list, vaccine =None):
    if vaccine == None:
        vaccine = input()
    if vaccine not in list:
        print(vaccine,'we have not this vaccine!\n'
              'try again: ')
        return validate_vaccine(list)
    return vaccine

def validate_id(func):
    @wraps(func)
    def wrapper(*args):
        if int(args[1]) >= 0:
            return func(args[0], args[1])
        else:
            print(args[1],'value must be positive!\n'
              'try again: ')
            return wrapper(args[0], input())
    return wrapper

def validate_numb(func):
    @wraps(func)
    def wrapper(*args):
        if not isinstance(args[1], int):
            try:
                return func(args[0], int(args[1]))
            except:
                print(args[1],'value must be integer!\n'
              'try again: ')
                return wrapper(args[0], input())
        else:
            return func(args[0], int(args[1]))

    return wrapper

def name_validation(func):
    @wraps(func)
    def wrapper(*args):
        if not (args[1].isalpha()):
            print(args[1], 'must consist of letters!\n'
                           'try again: ')
            return wrapper(args[0], input())
        else:
            return func(*args)

    return wrapper



def validate_phone(func):
    @wraps(func)
    def wrapper(*args):
        if not isinstance(args[1], int):
            code = '+'
            ph = args[1]
            new = ph.replace(code,'')
            try:
                new = int(new)
            except:
                print(args[1],'check number type!\n'
                              'try again:')
                return wrapper(args[0], input())
            if len(str(ph)) != 13:
                print(args[1],'check number length!\n' 
                               'try again')
                return wrapper(args[0], input())
            return func(*args)
        else:
            print(args[1],'smth went wrong!\n'
                          'try again: ')
            return wrapper(args[0], input())

    return wrapper

def validate_vaccine(list):
    def validate(func):
        @wraps(func)
        def wrapper(*args):
            if args[1] in list:
                return func(*args)
            else:
                print(args[1],'we have not this vaccine!\n'
                             'try again: ')
                return wrapper(args[0], input())

        return wrapper
    return validate


def validate_date(func):
    @wraps(func)
    def wrapper(*args):
        if isinstance(args[1], str):
            try:
                return func(args[0], datetime.datetime.strptime(args[1], '%d/%m/%Y'))
            except:
                print(args[1],'wrong format of date!\n'
                  'try again:')
                return wrapper(args[0], input())
        else:
            print(args[1],'check format of date!\n'
                  'try again:')
            return wrapper(args[0], input())
    return wrapper


def validate_time(func):
    @wraps(func)
    def wrapper(*args):
        if isinstance(args[1], str):
            try:
                return func(args[0], datetime.datetime.strptime(args[1], '%H:%M'))
            except:
                print(args[1],'wrong format of time!\n'
                  'try again:')
                return wrapper(args[0], input())
        else:
            print(args[1],'check format of time!\n'
                  'try again:')
            return wrapper(args[0], input())
    return wrapper

