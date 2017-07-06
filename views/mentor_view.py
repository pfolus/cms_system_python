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

