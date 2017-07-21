from models.manager_model import Manager
from models.student_model import Student
from models.mentor_model import Mentor
from models.accountant_model import Accountant
from views import codecooler_view


def edit_profile(login):
    codecoolers = Mentor.mentors + Manager.managers + Student.students + Accountant.accountants
    change_password(codecoolers, login)


def change_password(codecoolers, login):
    password = ''
    for user in codecoolers:
        if user.login == login:
            password = codecooler_view.ask_password()
            user.password = password
            codecooler_view.print_change_password_info()


def get_correct_login():
    login = codecooler_view.get_codecooler_login()

    while not check_if_login_exists(login):
        mentor_view.print_not_exist()
        login = codecooler_view.get_student_login()
    return login


def check_if_login_exists(login):
    login_exist = False

    for item in Student.students + Mentor.mentors + Accountant.accountants + Manager.managers:
        if item.login == login:
            login_exist = True

    return login_exist


def show_logins():
    print('\nLogin list: ')
    for user in Student.students + Mentor.mentors + Accountant.accountants + Manager.managers:
        codecooler_view.print_login(user)
