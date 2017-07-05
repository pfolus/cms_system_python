import os.path
import csv 
from models.student_model import Student
from models.mentor_model import Mentor
from models.manager_model import Manager
from models.accountant_model import Accountant
from views.codecooler_view import *
from controllers.codecoolers_list_controller import *
import manager_controler
import accountant_controller
import mentor_controller
import student_controller



def start_controller():
    cc_list_object = CodecoolersList()
    codecoolers_records = read_codecoolers_list_csv()
    create_codecoolers(codecoolers_records)


def read_codecoolers_list_csv():

    with open (os.path.dirname(__file__) + '../csv_databases/codecoolers_list.csv', 'r') as file:
        reader = csv.reader(file, delimiter='|')
        
        codecoolers_list = []

        for line in reader:
            codecoolers_list.append(line)

    create_codecoolers()


def create_codecoolers(cc_list_object, codecoolers_records):

    LOGIN_INDEX = 0
    PASSWORD_INDEX = 1
    NAME_INDEX = 2
    SURNAME_INDEX = 3
    TYPE_INDEX = 4

    OBEJECT_STRING = 'user[TYPE_INDEX](user[LOGIN_INDEX], user[PASSWORD_INDEX], user[NAME_INDEX], user[SURNAME_INDEX])'

    for user in read_codecoolers_records:
        add_user_to_list(cc_list_obbject, eval(OBEJECT_STRING))


def add_user_to_list(cc_list_object, user):

    class_name = user.__class__.__name__

    if class_name == "Student":
        cc_list_object.students_list.append(user)
    elif class_name == "Mentor":
        cc_list_object.mentors_list.append(user)
    elif class_name == "Accountant":
        cc_list_object.accountants_list.append(user)
    elif class_name == "Manager":
        cc_list_object.managers_list.append(user)


def login(): 

    login = get_login()
    password = get_password()
    codecoolers_list = read_codecoolers_list_csv()

    LOGIN_INDEX = 0
    PASSWORD_INDEX = 1

    for user in codecoolers_list:
        if user[LOGIN_INDEX] == login and user[PASSWORD_INDEX] == password:
            return user[LOGIN_INDEX]


