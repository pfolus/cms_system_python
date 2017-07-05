import datetime
import csv
import datetime
from models.codecooler_model import *
#from models.student_model import Student
#from models.mentor_model import Mentor
from models.manager_model import Manager
from models.accountant_model import Accountant
from models.canvas_model import Canvas
from models.assingment_model import Assingment
from models.submission_model import Submission
from views.codecooler_view import *
from views.canvas_view import *
from controllers import manager_controller
from controllers import student_controller
from controllers import accountant_controller
from controllers import mentor_controller


def start_controller():
    canvas = Canvas()
    load_codecoolers_list_csv(canvas)
    load_assingments_list_csv(canvas)
    load_submissions_list_csv(canvas)
    user = login(canvas)
    run_controller(user, canvas)
    export_data_to_csv(canvas)


def load_submissions_list_csv(canvas):

    with open('csv_databases/submissions.csv', 'r') as file:
        reader = csv.reader(file, delimiter='|')

        submissions = []

        for line in reader:
            line[3] = datetime.datetime.strptime(line[3], '%d.%m.%Y')
            line[4] = int(line[4])
            submissions.append(line)

    create_and_add_submissions_objects(submissions, canvas)


def create_and_add_submissions_objects(submissions, canvas):

    for item in submissions:
        canvas.submissions.append(Submission(item[0], item[1], item[2], item[3], item[4], item[5]))


def load_assingments_list_csv(canvas):

    with open ('csv_databases/assingments.csv', 'r') as file:
        reader = csv.reader(file, delimiter='|')

        assingments = []

        for line in reader:
            line[2] = datetime.datetime.strptime(line[2], '%d.%m.%Y')
            line[3] = int(line[3])
            assingments.append(line)

    create_and_add_assingments_objects(assingments, canvas)


def create_and_add_assingments_objects(assingments, canvas):

    TITLE_INDEX = 0
    CONTENT_INDEX = 1
    RATE_INDEX = 2
    MAXGRADE_INDEX = 3

    for item in assingments:
        canvas.assingments.append(Assingment(item[0], item[1], item[2], item[3]))


def load_codecoolers_list_csv(canvas):

    with open ('csv_databases/codecoolers_list.csv', 'r') as file:
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

    for user in codecoolers_list:
        #if user[TYPE_INDEX] == "Student":
            #add_user_to_list(canvas, Student(user[LOGIN_INDEX], user[PASSWORD_INDEX], user[NAME_INDEX], user[SURNAME_INDEX]))
        if user[TYPE_INDEX] == "Manager":
            add_user_to_list(canvas, Manager(user[LOGIN_INDEX], user[PASSWORD_INDEX], user[NAME_INDEX], user[SURNAME_INDEX]))
        elif user[TYPE_INDEX] == "Accountant":
            add_user_to_list(canvas, Accountant(user[LOGIN_INDEX], user[PASSWORD_INDEX], user[NAME_INDEX], user[SURNAME_INDEX]))
        #elif user[TYPE_INDEX] == "Mentor":
            #add_user_to_list(canvas, Mentor(user[LOGIN_INDEX], user[PASSWORD_INDEX], user[NAME_INDEX], user[SURNAME_INDEX]))


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

    show_login_menu()
    login = get_login()
    password = get_password()

    LOGIN_INDEX = 0
    PASSWORD_INDEX = 1

    summary_list = canvas.mentors + canvas.managers + canvas.students + canvas.accountants

    for user in summary_list:
        if user.login == login and user.password == password:
            return user


def run_controller(user, canvas):

    class_name = user.__class__.__name__

    if class_name == 'Student':
        student_controller.start_controller(canvas, user)
    if class_name == 'Mentor':
        mentor_controller.start_controller(canvas, user)
    if class_name == 'Accountant':
        accountant_controller.start_controller(canvas, user)
    if class_name == 'Manager':
        manager_controller.start_controller(canvas, user)


def export_data_to_csv(canvas):

    export_submissions(canvas.submissions)
    export_assingments(canvas.assingments)
    '''for codecoolers in [canvas.mentors,
                        canvas.managers,
                        canvas.students,
                        canvas.accountants]:
        export_codecooler(codecoolers)'''


def export_submissions(submissions):

    with open('csv_databases/submissions.csv', 'w') as file:

        writer = csv.writer(file, delimiter = '|')
        for submission in submissions:
            writer.writerow([submission.user_login,
                                submission.title,
                                submission.answer,
                                submission.date.strftime('%d.%m.%Y'),
                                str(submission.score),
                                str(submission.is_checked)])


def export_assingments(assingments):

    with open ('csv_databases/assingments.csv', 'w') as file:

        writer = csv.writer(file, delimiter = '|')
        for assingment in assingments:
            writer.writerow([assingment.title,
                                assingment.content,
                                assingment.date.strftime('%d.%m.%Y'),
                                str(assingment.max_grade)])


def export_codecooler(codecoolers):
    with open ('csv_databases/codecoolers_list.csv', 'w') as file:

        writer = csv.writer(file, delimiter = '|')
        for codecooler in codecoolers:
            writer.writerow([codecooler.login,
                            codecooler.password,
                            codecooler.name,
                            codecooler.surname])
