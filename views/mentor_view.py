from datetime import datetime
from models.mentor_model import Mentor
from models.student_model import Student
from models.submission_model import Submission


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
            '(7).Shoutbox message',
            '(8).Change password',
            '(9).Add an event',
            '(10).Show upcoming events',
            '(11).Remove an event',
            '(12).Private message',
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


def show_logins():
    '''
    Prints all student logins.

    Paramaters
    ----------
    None

    Returns
    -------
    None
    '''

    print('\nLogin list: ')
    for user in Student.students:
        print('-> {}'.format(user.login))


def show_submissions():
    '''
    Prints all submissions title and author.

    Paramaters
    ----------
    None

    Returns
    -------
    None
    '''


    print('\nSubmissions list: \n')
    index = 0
    for submission in Submission.submissions:
        if submission.is_checked == 'True':
            print('{}.Student -> {} | Submission title -> {} (Already rated)'.format(
                index, submission.user_login, submission.title))
        else:
            print('{}.Student -> {} | Submission title -> {}'.format(
                index, submission.user_login, submission.title))
        index += 1


def get_submission():
    '''
    Asks for submission index, and pick chosen submission.

    Paramaters
    ----------
    None

    Returns
    -------
    Submission.submissions[submission_index] = object of Submission class
    '''

    submission_index = get_int('Pick submission index: ')
    while submission_index not in range(len(Submission.submissions)):
        print('There is no such submission index')
        submission_index = get_int('Pick submission index: ')

    return Submission.submissions[submission_index]


def show_fullnames():
    '''
    Shows all students full names.

    Paramaters
    ----------
    None

    Returns
    -------
    None
    '''

    index = 0
    print('\nPresence List: \n')
    for user in Student.students:
        print('{} -> {} {}'.format(index, user.name, user.surname))
        index += 1


def print_grades_range_info(max_grade):
    print('Grade must be in range <-3:{}>'.format(max_grade))


def show_numbered_student(index, name, surname):
    print('\nStudent name:\n\n{}. {} {}'.format(index, name, surname))


def ask_for_late():

    return input("Has she/he come yet? (y/n): ")


def attendance_checked():

    print("\nAttendance checked!")


def print_attendance_menu():
    '''
    Prints menu
    '''

    menu = ['\n(1) Present!',
            '(2) Late!',
            '(3) Absent!']

    for item in menu:
        print(item)
