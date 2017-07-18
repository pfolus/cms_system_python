import csv
import datetime
from models.manager_model import Manager
from models.student_model import Student
from models.mentor_model import Mentor
from models.accountant_model import Accountant
from models.assingment_model import Assingment
from models.submission_model import Submission
from models.attendance_model import Attendance


def load_attendances_list_csv():

    with open('csv_databases/attendances.csv', 'r') as file:
        reader = csv.reader(file, delimiter='|')

        for line in reader:
            login = line[0]
            average = line[1]
            date = datetime.datetime.strptime(line[2], '%d.%m.%Y')

            Attendance(login, value, date)


def load_submissions_list_csv():

    with open('csv_databases/submissions.csv', 'r') as file:
        reader = csv.reader(file, delimiter='|')

        submissions = []

        for line in reader:
            line[3] = datetime.datetime.strptime(line[3], '%d.%m.%Y')
            line[4] = int(line[4])
            submissions.append(line)

    create_and_add_submissions_objects(submissions)


def create_and_add_submissions_objects(submissions):

    for item in submissions:
        if item[5] == 'False':
            Submission(item[0], item[1], item[2], item[3], item[4], '')
        else:
            Submission(item[0], item[1], item[2], item[3], item[4], item[5])


def load_assingments_list_csv():

    with open('csv_databases/assingments.csv', 'r') as file:
        reader = csv.reader(file, delimiter='|')

        assingments = []

        for line in reader:
            line[2] = datetime.datetime.strptime(line[2], '%d.%m.%Y')
            line[3] = int(line[3])
            assingments.append(line)

    create_and_add_assingments_objects(assingments)


def create_and_add_assingments_objects(assingments):

    TITLE_INDEX = 0
    CONTENT_INDEX = 1
    RATE_INDEX = 2
    MAXGRADE_INDEX = 3

    for item in assingments:
        canvas.assingments.append(Assingment(item[0], item[1], item[2], item[3]))


def load_codecoolers_list_csv(canvas):

    with open('csv_databases/codecoolers_list.csv', 'r') as file:
        reader = csv.reader(file, delimiter='|')

        codecoolers_list = []

        for line in reader:
            codecoolers_list.append(line)

    create_codecoolers_objects(codecoolers_list)


def create_codecoolers_objects(codecoolers_list):

    LOGIN_INDEX = 0
    PASSWORD_INDEX = 1
    NAME_INDEX = 2
    SURNAME_INDEX = 3
    TYPE_INDEX = 4

    # creates object codecooler from nested list 'codecoolers_list: user(user[login_index], user[password_index]...'

    for user in codecoolers_list:
        if user[TYPE_INDEX] == "Student":
            Student(user[LOGIN_INDEX], user[PASSWORD_INDEX], user[NAME_INDEX], user[SURNAME_INDEX])
        if user[TYPE_INDEX] == "Manager":
            Manager(user[LOGIN_INDEX], user[PASSWORD_INDEX], user[NAME_INDEX], user[SURNAME_INDEX])
        elif user[TYPE_INDEX] == "Accountant":
            Accountant(user[LOGIN_INDEX], user[PASSWORD_INDEX], user[NAME_INDEX], user[SURNAME_INDEX])
        elif user[TYPE_INDEX] == "Mentor":
            Mentor(user[LOGIN_INDEX], user[PASSWORD_INDEX], user[NAME_INDEX], user[SURNAME_INDEX])


def export_data_to_csv():

    export_submissions()
    export_assingments()
    save_atendances_list_csv()
    codecoolers = Mentor.mentors + Manager.managers + Student.students + Accountant.accountants
    export_codecooler(codecoolers)


def export_submissions():

    with open('csv_databases/submissions.csv', 'w') as file:

        writer = csv.writer(file, delimiter='|')
        for submission in Submission.submissions:
            if submission.is_checked:
                writer.writerow([submission.user_login,
                                submission.title,
                                submission.answer,
                                submission.date.strftime('%d.%m.%Y'),
                                str(submission.score),
                                'True'])
            else:
                writer.writerow([submission.user_login,
                                submission.title,
                                submission.answer,
                                submission.date.strftime('%d.%m.%Y'),
                                str(submission.score),
                                'False'])


def export_assingments():

    with open('csv_databases/assingments.csv', 'w') as file:

        writer = csv.writer(file, delimiter='|')
        for assingment in Assingment.assingments:
            writer.writerow([assingment.title,
                             assingment.content,
                             assingment.date.strftime('%d.%m.%Y'),
                             str(assingment.max_grade)])


def export_codecooler(codecoolers):
    with open('csv_databases/codecoolers_list.csv', 'w') as file:

        writer = csv.writer(file, delimiter='|')
        for codecooler in codecoolers:
            writer.writerow([codecooler.login,
                            codecooler.password,
                            codecooler.name,
                            codecooler.surname,
                            codecooler.__class__.__name__])


def save_atendances_list_csv():

    with open('csv_databases/attendances.csv', 'w') as file:
        writer = csv.writer(file, delimiter='|')

        for attendance in Attendance.attendances:
            writer.writerow([attendance.student_login,
                             attendance.average,
                             ",".join([str(number) for number in attendance.student_attendances])])
