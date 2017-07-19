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
