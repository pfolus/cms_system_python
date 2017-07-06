from views.assingment_view import *
from views.bcolors import Bcolors
from views.codecooler_view import *


def show_menu():
    menu = ['1. Show my grades',
            '2. Submit assingment',
            '0. Log out']
    for line in menu:
        print(line)


def choose_function():
    '''
    Asks an user for a number, representing function,
    and returns it
    '''
    DEFAULT_VALUE = ''
    choice = DEFAULT_VALUE
    possible_choices = [0, 1, 2]

    while choice not in possible_choices:
        try:
            choice = int(input('Choose function: '))
        except ValueError:
            print('Wrong choice.')

    return choice


def show_assingments(assingments):
    number = 0
    print('\nAll assingments:\n')
    for assingment in assingments:
        show_assingment(assingment, number)
        number += 1

    return number


def get_assingment_number():
    choice = int(input("Choose assingment: "))

    return choice


def error_number():
    print('Wrong number.')


def print_assingment_done():
    print(Bcolors.HEADER + 'You have already done this assingment' + Bcolors.ENDC)


def get_answer():
    answer = input('Type the answer (preferably link to repo on github.com): ')

    return answer


def info_submission_added():
    print('Your new submission was added succesfully.')
