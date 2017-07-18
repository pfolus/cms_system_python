def print_menu():
    '''
    Prints manager submenu
    '''

    print('''1. List mentors
2. List mentors with details
3. Add mentor
4. Remove mentor
5. List students
6. List students with details
0. Log out
''')


def ask_for_option():
    '''
    Get user inputfor choosing option in menu

    Returns:
        string
    '''

    return input("Choose option: ")


def option_error():
    '''
    Print error message
    '''

    print("There isn't such option!")


def show_mentors_with_details(mentors):
    '''
    Prints all mentors' details

    Args:
        mentors - list with objects
    '''

    index = 1
    print()
    for mentor in mentors:
        print("({}) {} {} - {}".format(index, mentor.name,
                                      mentor.surname, mentor.login))
        index += 1
    print()


def show_mentors(mentors):
    '''
    Prints all mentors

    Args:
        mentors - list with objects
    '''

    index = 1
    print()
    for mentor in mentors:
        print("({}) {} {}".format(index, mentor.name, mentor.surname))
        index += 1
    print()


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


def ask_for_index():
    '''
    Gets index input from user and convert it to int

    Rturns:
        int
    '''

    is_correct = False

    while not is_correct:
        try:
            index = int(input("Enter index: "))
            if index < 1:
                option_error()
            else:
                is_correct = True
        except ValueError:
            option_error()

    return index - 1
