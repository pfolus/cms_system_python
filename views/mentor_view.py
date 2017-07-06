from controllers.mentor_controller import *
from models.mentor_model import Mentor

def print_welcome(user):
    print('\n' +'Witamy Szanownego kolegę {}a!'.format(user.name))


def print_menu():
    menu = ['========================',
            '(1).View student details',
            '(2).Add assignment',
            '(3).Grade assignment',
            '(4).Check attendance',
            '(5).Remove Student',
            '(6).Add student',
            '(0).Exit',
            '========================']
    for option in menu:
        print(option)


def get_choice():
    return input('Enter your choice: ')


def print_bad_choice():
    print('\n' + 'There is no such option, try again!')


def get_login():

    login = input('\nEnter student login: ')

    while len(login) < 6:
        print('Login must have at least 6 characters, try again!')
        login = input('\nEnter student login: ')

    return login


def get_password():

    password = input('\nEnter student password: ')

    while (len(password) < 6) or (has_digit(password) == 0):
        print('Password must have at least 6 characters and 1 digit, try again!')
        password = input('\nEnter student password: ')

    return password


def get_name():

    name = input('\nEnter student name: ')

    while (len(name) < 3) or (has_digit(name) == 1):
        print('No digits allowed!')
        print('Name must have at least 3 characters, try again!')
        name = input('\nEnter student name: ')

    return name


def get_surname():

    surname = input('\nEnter student surname: ')

    while len(surname) < 3 or (has_digit(surname) == 1):
        print('No digits allowed!')
        print('Surname must have at least 3 characters, try again!')
        surname = input('\nEnter student surname: ')

    return surname


def has_digit(item):
    has_digit = 0
    for char in item:
        if char.isdigit():
            has_digit = 1

    return has_digit


def get_student_name():
    return input('\nType student login: ')