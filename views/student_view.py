from views.assingment_view import *
from views.bcolors import Bcolors
from views.codecooler_view import *


def show_menu():
    '''
    Prints every option of menu in new line
    '''
    menu = ['1. Show my grades',
            '2. Submit assingment',
            '0. Log out\n']
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
    '''
    Prints every possible assingment in new line
    and returns their amount

    Paramaters
    ----------
    assingments = list (of Assingment objects)

    Returns
    -------
    number = int
    '''
    amount_of_assingments = 0
    print(Bcolors.BLUE + '\nAll assingments:\n' + Bcolors.ENDC)
    for assingment in assingments:
        show_assingment(assingment, amount_of_assingments)
        amount_of_assingments += 1

    return amount_of_assingments


def get_assingment_number():
    '''
    Gets int input, representing chosen assingment and returns it
    '''
    choice = int(input("Choose assingment: "))

    return choice


def error_number():
    '''
    Prints info about providing wrong number
    '''
    print('Wrong number.')


def print_assingment_done():
    '''
    Prints info about done assingment
    '''
    print(Bcolors.BOLD + '\nYou have already done this assingment' + Bcolors.ENDC)


def get_answer():
    '''
    Gets an answer for submission and returns it
    '''
    answer = input(Bcolors.UNDERLINE + 'Type the answer (preferably link to repo on github.com): ' + Bcolors.ENDC)

    return answer


def info_submission_added():
    '''
    Prints an info about adding submission
    '''
    print('Your new submission was added succesfully.')


def show_grades_info(grades_sum, max_grades_sum, amount_of_grades):
    '''
    Prints info about student's grades

    Paramaters
    ----------
    grades_sum = int
    max_grades_sum = int
    amount_of_grades = int

    Returns
    -------
    None
    '''
    print(Bcolors.BOLD + '\nYou have {} grades.\nYour score: {}/{}\n'.format(amount_of_grades, grades_sum, max_grades_sum) + Bcolors.ENDC)
