import os.path
import csv
from models.student_model import Student
from models.mentor_model import Mentor
from models.manager_model import Manager
from models.accountant_model import Accountant
from models.canvas_model import Canvas
from views.codecooler_view import *
import manager_controler
import student_controller
import accountant_controller
import mentor_controller



def start_controller():
    canvas = Canvas()
    load_codecoolers_list_csv(canvas)
    load_assigments_list_csv(canvas)
    load_submissions_list_csv(canvas)
    user = login(canvas)
    run_controler(user, canvas)


def load_submissions_list_csv(canvas):

    with open (os.path.dirname(__file__) + '../csv_databases/submissions.csv', 'r') as file:
        reader = csv.reader(file, delimiter='|')
        
        submissions = []

        for line in reader:
            submissions.append(line)

    create_and_add_submissions_objects(submissions, canvas)

def create_and_add_submissions_objects(submissions, canvas):

    # creates object assigment from nested list assigment
    OBJECT_STRING = 'Submission(item[0], item[1], item[2], item[3], item[4], item[5])'

    for item in submissions:
        canvas.submissions.append(eval(OBJECT_STRING))


def load_assigments_list_csv(canvas):

    with open (os.path.dirname(__file__) + '../csv_databases/assigments.csv', 'r') as file:
        reader = csv.reader(file, delimiter='|')
        
        assigments = []

        for line in reader:
            assigments.append(line)

    create_and_add_assigments_objects(assigments, canvas)

def create_and_add_assigments_objects(assigments, canvas):

    TITLE_INDEX = 0
    CONTENT_INDEX = 1
    RATE_INDEX = 2
    MAXGRADE_INDEX = 3

    # creates object assigment from nested list assigment
    OBJECT_STRING = 'Assigment(item[0], item[1], item[2], item[3])'

    for item in assigments:
        canvas.assigments.append(eval(OBJECT_STRING))



def load_codecoolers_list_csv(canvas):

    with open (os.path.dirname(__file__) + '../csv_databases/codecoolers_list.csv', 'r') as file:
        reader = csv.reader(file, delimiter='|')
        
        codecoolers_list = []

        for line in reader:
            codecoolers_list.append(line)

    create_codecoolers_objects(codecoolers_list, canvas)


def create_codecoolers_objects(codecoolers_list, canvas):

    LOGIN_INDEX = 0
    PASSWORD_INDEX = 1
    NAME_INDEX = 2
    SURNAME_INDEX = 3
    TYPE_INDEX = 4

    # creates object codecooler from nested list 'codecoolers_list: user(user[login_index], user[password_index]...'
    OBJECT_STRING = 'user[TYPE_INDEX](user[LOGIN_INDEX], user[PASSWORD_INDEX], user[NAME_INDEX], user[SURNAME_INDEX])'

    for user in codecoolers_list:
        add_user_to_list(canvas, eval(OBJECT_STRING))


def add_user_to_list(canvas, user):

    class_name = user.__class__.__name__

    if class_name == "Student":
        canvas.students.append(user)
    elif class_name == "Mentor":
        canvas.mentors.append(user)
    elif class_name == "Accountant":
        canvas.accountants.append(user)
    elif class_name == "Manager":
        canvas.managers.append(user)


def login(canvas):

    login = get_login()
    password = get_password()

    LOGIN_INDEX = 0
    PASSWORD_INDEX = 1

    for user in zip(canvas.mentors, canvas.managers, canvas.studens, canvas.accountants):
        if user.login == login and user.password == password:
            return user


def run_controller(user, canvas):

    class_name = user.__class__.__name__

    if class_name == 'Student':
        student_controller.start_controller(user, canvas)
    if class_name == 'Mentor':
        mentor_controller.start_controller(user, canvas)
    if class_name == 'Accountant':
        accountant_controller.start_controller(user, canvas)
    if class_name == 'Manager':
        manager_controller.start_controller(user, canvas)


