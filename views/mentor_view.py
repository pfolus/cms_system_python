from controllers.mentor_controller import *
from models.mentor_model import Mentor
from views.employee_view import *
from datetime import datetime
from models.student_model import Student
from models.canvas_model import Canvas
from models.submission_model import Submission

def print_welcome(user):
    '''
    Prints welcome message

    Paramaters
    ----------
    user = obj of Mentor class

    Returns
    -------
    None
    '''
    print('\n' +'Witamy Szanownego kolegę {}a!'.format(user.name))

def print_menu():
    '''
    Prints menu
    '''
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
    '''
    asks for choice

    Returns
    -------
    input string
    '''
    return input('Enter your choice: ')


def print_bad_choice():
    '''
    Prints error message
    '''
    print('\n' + 'There is no such option, try again!')


def get_login():
    ''' 
    asks for login until its longer than 5 characters

    Returns
    -------
    login = string
    '''
    login = input('\nEnter student login: ')

    while len(login) < 6:
        print('Login must have at least 6 characters, try again!')
        login = input('\nEnter student login: ')

    return login


def get_password():
    ''' 
    asks for password until its longer than 5 characters and have 
    at least 1 digit

    Returns
    -------
    password = string
    '''
    password = input('\nEnter student password: ')

    while (len(password) < 6) or (has_digit(password) == 0):
        print('Password must have at least 6 characters and 1 digit, try again!')
        password = input('\nEnter student password: ')

    return password


def get_name():
    ''' 
    asks for name until its longer than 3 characters. Checks if 
    name have digits, if so it asks again.

    Returns
    -------
    name = string
    '''
    name = input('\nEnter student name: ')

    while (len(name) < 3) or (has_digit(name) == 1):
        print('No digits allowed!')
        print('Name must have at least 3 characters, try again!')
        name = input('\nEnter student name: ')

    return name


def get_surname():
    ''' 
    asks for surname until its longer than 3 characters. Checks if 
    name have digits, if so it asks again.

    Returns
    -------
    surname = string
    '''
    surname = input('\nEnter student surname: ')

    while len(surname) < 3 or (has_digit(surname) == 1):
        print('No digits allowed!')
        print('Surname must have at least 3 characters, try again!')
        surname = input('\nEnter student surname: ')

    return surname


def has_digit(item):
    ''' 
    Checks if item has digit.

    Paramaters
    ----------
    item = string

    Returns
    -------
    has_digit = int (0 or 1)
    '''

    has_digit = 0
    for char in item:
        if char.isdigit():
            has_digit = 1

    return has_digit


def get_student_login():
    return input('\nType student login: ')


def print_not_exist():
    print('login does not exist, try again!')


def print_done():
    print('\nOperation done\n')


def get_string(item):
    return input('\nEnter {}: '.format(item))


def get_date():
    ''' 
    Asks for date until date with correct format passed.
    If not, prints error message.

    Returns
    -------
    correct_date = datetime object
    '''

    while True:
        date = input('Enter date in format dd.mm.yyyy: ')
        try:
            correct_date = datetime.strptime(date, '%d.%m.%Y')
            return correct_date
        except ValueError:
            print('Wrong input!')


def get_int(message):
    ''' 
    Asks for input until digits provided. Otherwise,
    error massage printed.

    Paramaters
    ----------
    message = string

    Returns
    -------
    max_grade = int
    '''
    while True:
        try:
            max_grade = int(input(message))
            return max_grade
        except ValueError:
            print('Wrong input!')


def show_logins(canvas):
    ''' 
    Prints all student logins.

    Paramaters
    ----------
    canvas = object of Canvas class

    Returns
    -------
    None
    '''

    print('\nLogin list: ')
    for user in canvas.students:
        print('-> {}'.format(user.login))


def show_submissions(canvas):
    ''' 
    Prints all submissions title and author.

    Paramaters
    ----------
    canvas = object of Canvas class

    Returns
    -------
    None
    '''


    print('\nSubmissions list: \n')
    index = 0
    for submission in canvas.submissions:
        if submission.is_checked == 'True':
            print('{}.Student -> {} | Submission title -> {} (Already rated)'.format(
                index, submission.user_login, submission.title))
        else:
            print('{}.Student -> {} | Submission title -> {}'.format(
                index, submission.user_login, submission.title))
        index += 1


def get_submission(canvas):
    ''' 
    Asks for submission index, and pick chosen submission.

    Paramaters
    ----------
    canvas = object of Canvas class

    Returns
    -------
    canvas.submissions[submission_index] = object of Submission class
    '''

    submission_index = get_int('Pick submission index: ')
    while submission_index not in range(len(canvas.submissions)):
        print('There is no such submission index')
        submission_index = get_int('Pick submission index: ')

    return canvas.submissions[submission_index]


def show_fullnames(canvas):
    '''
    Shows all students full names.

    Paramaters
    ----------
    canvas = object of Canvas class

    Returns
    -------
    None
    '''

    index = 0
    print('\nPresence List: \n')
    for user in canvas.students:
        print('{} -> {} {}'.format(index, user.name, user.surname))
        index += 1


def print_grades_range_info(max_grade):
    print('Grade must be in range <-3:{}>'.format(max_grade))


def show_numbered_student(index, name, surname):
    print('\nStudent name:\n\n{}. {} {}'.format(index, name, surname))


def print_attendance_menu():
    '''
    Prints menu
    '''

    menu = ['\n==================',
            '(1)-->insert absence',
            '(2)-->insert late',
            '(3)-->insert presence',
            '==================']

    for item in menu:
        print(item)
