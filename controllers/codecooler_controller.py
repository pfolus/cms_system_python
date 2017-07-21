from models.manager_model import Manager
from models.student_model import Student
from models.mentor_model import Mentor
from models.accountant_model import Accountant
from views import codecooler_view


def edit_profile(login):
    '''
    Changes password of user with given login

    Args:
        login - string
    '''
    codecoolers = Mentor.mentors + Manager.managers + Student.students + Accountant.accountants
    change_password(codecoolers, login)


def change_password(codecoolers, login):
    '''
    Changes password of user with given login

    Args:
        login - string
        codecoolers - all users list
    '''
    password = ''
    for user in codecoolers:
        if user.login == login:
            password = codecooler_view.ask_password()
            user.password = password
            codecooler_view.print_change_password_info()


def get_correct_login():
    '''
    Asks for correct login of user

    Returns:
        login - string
    '''
    login = codecooler_view.get_codecooler_login()

    while not check_if_login_exists(login):
        mentor_view.print_not_exist()
        login = codecooler_view.get_student_login()
    return login


def check_if_login_exists(login):

    '''
    Checks if login exists in logins list

    Args:
        login - string

    Returns:
        bool
    '''

    login_exist = False

    for item in Student.students + Mentor.mentors + Accountant.accountants + Manager.managers:
        if item.login == login:
            login_exist = True

    return login_exist


def show_logins():
    '''
    Prints list with logins
    '''
    print('\nLogin list: ')
    for user in Student.students + Mentor.mentors + Accountant.accountants + Manager.managers:
        codecooler_view.print_login(user)
