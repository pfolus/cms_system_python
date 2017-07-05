<<<<<<< HEAD
from models.student_model import Student
from models.mentor_model import Mentor
from models.manager_model import Manager
from models.accountant_model import Accountant
=======
<<<<<<< Updated upstream
=======
from views.codecooler_view import *
from controllers.codecoolers_list_controller import *
from controllers.accountant_controller import *
from controllers.mentor_controller import *
from controllers.manager_controller import *
from controllers.student_controller import *


def login():

    login = get_login()
    password = get_password()
    codecoolers_list = read_codecoolers_list_csv()

    LOGIN_INDEX = 0
    PASSWORD_INDEX = 1
    TYPE_INDEX = 4

    for user in codecoolers_list:
        if user[LOGIN_INDEX] == login and user[PASSWORD_INDEX] == password:
            #return user[LOGIN_INDEX]
            login = user[TYPE_INDEX]
            if user[TYPE_INDEX] == 'Student':
                student_panel(login)
            if user[TYPE_INDEX] == 'Accountant':
                accountant_panel(login)
            if user[TYPE_INDEX] == 'Mentor':
                mentor_panel(login)
            if user[TYPE_INDEX] == 'Manager':
                manager_panel(login)

>>>>>>> Stashed changes
>>>>>>> master
