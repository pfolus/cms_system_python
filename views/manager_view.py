from views.employee_view import *


def greet(user):
    print('Hey {}!'.format(user.name))


def print_menu():

    print('''1. List mentors
2. List mentors with details
3. Add mentor
4. Remove mentor
5. List students
6. List students with details
0. Log out
          ''')


def ask_for_option():

    return input("Choose option: ")


def option_error():

    print("There isn't such option!")


def show_mentors_with_details(mentors):

    index = 1

    for mentor in mentors:
        print("{}. {} {} - {}".format(index, mentor.name,
                                      mentor.surname, mentor.login))
        index += 1


def show_mentors(mentors):

    index = 1

    for mentor in mentors:
        print("{}. {} {}".format(index, mentor.name, mentor.surname))
        index += 1


def ask_name():

    name = input("Name: ")

    while len(name) < 1 and not name.isalpha():
        print("Wrong input!")
        name = input("Name: ")

    return name


def ask_surname():

    surname = input("Surame: ")

    while len(surname) < 1 and not surname.isalpha():
        print("Wrong input!")
        name = input("Surame: ")

    return surname


def ask_login():

    login = input("Login: ")

    while len(login) < 1:
        print("Wrong input!")
        login = input("Login: ")

    return login


def ask_password():

    password = input("Password: ")

    while len(password) < 4:
        print("Minimum 4 characters!")
        password = input("Password: ")

    return password


def ask_for_index():

    index = input("Choose mentor index: ")

    while not index.isdigit():
        print("Enter proper index!")
        index = input("Choose mentor index: ")

    return int(index)
