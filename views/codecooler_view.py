from views.bcolors import Bcolors


def choose_function():
    '''
    Asks an user for a number, representing function,
    and returns it
    '''
    DEFAULT_VALUE = ''
    choice = DEFAULT_VALUE
    possible_choices = [0, 1, 2, 3]

    while choice not in possible_choices:
        try:
            choice = int(input('Choose function: '))
        except ValueError:
            print('Wrong choice.')

    return choice


def greet(user):
    '''
    Prints welcome message with logged user's name
    '''

    print(Bcolors.RED + Bcolors.BOLD + "\nHello " + user.name + "!\n" + Bcolors.ENDC)


def ask_name():
    '''
    Gets name input from user

    Rturns:
        string
    '''

    name = input("Name: ")

    while len(name) < 1 and not name.isalpha():
        print("Wrong input!")
        name = input("Name: ")

    return name


def ask_surname():
    '''
    Gets surname input from user

    Rturns:
        string
    '''

    surname = input("Surame: ")

    while len(surname) < 1 and not surname.isalpha():
        print("Wrong input!")
        name = input("Surame: ")

    return surname


def ask_login():
    '''
    Gets login input from user

    Rturns:
        string
    '''

    login = input("Login: ")

    while len(login) < 1:
        print("Wrong input!")
        login = input("Login: ")

    return login


def ask_password():
    '''
    Gets password input from user

    Rturns:
        string
    '''

    password = input("Password: ")

    while len(password) < 4:
        print("Minimum 4 characters!")
        password = input("Password: ")

    return password


def print_change_password_info():
    print(Bcolors.RED + '\nPassword was changed succesfully!\n' + Bcolors.ENDC)
