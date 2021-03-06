import csv
import datetime
from models.manager_model import Manager
from models.student_model import Student
from models.mentor_model import Mentor
from models.accountant_model import Accountant
from models.assingment_model import Assingment
from models.submission_model import Submission
from models.attendance_model import Attendance
from models.shoutbox_model import Shoutbox
from models.event_model import Event
from models.private_messages_model import PM
from controllers import event_controller


def load_data_from_csv():
    '''
    Runs all fucntions to load data from files
    '''

    load_assingments()
    load_codecoolers()
    load_events()
    load_submissions()
    load_attendances()


def export_data_to_csv():
    '''
    Runs all functions to export data to files
    '''

    export_submissions()
    export_assingments()
    export_attendances()
    codecoolers = Mentor.mentors + Manager.managers + Student.students + Accountant.accountants
    export_codecoolers(codecoolers)
    export_shoutbox_messages()
    export_events()
    export_PM()


def load_attendances():
    '''
    Loads data attendances from file
    '''

    with open('csv_databases/attendances.csv', 'r') as file:
        reader = csv.reader(file, delimiter='|')

        for line in reader:
            login = line[0]
            value = float(line[1])
            date = datetime.datetime.strptime(line[2], '%d.%m.%Y')
            date = date.date()

            Attendance(login, value, date)


def load_submissions():
    '''
    Loads data attendances from file
    '''


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


def load_assingments():
    '''
    Loads data assignments from file
    '''


    with open('csv_databases/assingments.csv', 'r') as file:
        reader = csv.reader(file, delimiter='|')

        assingments = []

        for line in reader:
            line[2] = datetime.datetime.strptime(line[2], '%d.%m.%Y')
            line[3] = int(line[3])
            assingments.append(line)

    create_and_add_assingments_objects(assingments)


def load_events():
    '''
    Loads data events from file
    '''


    with open('csv_databases/events.csv', 'r') as file:
        reader = csv.reader(file, delimiter='|')

        events = []

        for line in reader:
            line[1] = datetime.datetime.strptime(line[1], '%d.%m.%Y')
            events.append(line)

    create_and_add_events_objects(events)


def create_and_add_events_objects(events):
    '''
    Create events objects
    '''

    NAME = 0
    DATE = 1
    LOGIN = 2
    EVENT_TYPE = 3

    for ev in events:
        Event(ev[NAME], ev[DATE], ev[LOGIN], ev[EVENT_TYPE])


def create_and_add_assingments_objects(assingments):
    '''
    Create assingments objects
    '''

    TITLE_INDEX = 0
    CONTENT_INDEX = 1
    RATE_INDEX = 2
    MAXGRADE_INDEX = 3

    for item in assingments:
        Assingment(item[0], item[1], item[2], item[3])


def load_codecoolers():
    '''
    Loads data codecoolers from file
    '''


    with open('csv_databases/codecoolers_list.csv', 'r') as file:
        reader = csv.reader(file, delimiter='|')

        codecoolers_list = []

        for line in reader:
            codecoolers_list.append(line)

    create_codecoolers_objects(codecoolers_list)


def load_shoutbox_messages():
    '''
    Loads data shoutbox_messages from file
    '''

    with open('csv_databases/shoutbox.csv', 'r') as file:
        reader = csv.reader(file, delimiter='|')

        messages = []

        for line in reader:
            line[0] = datetime.datetime.strptime(line[0], '%d.%m.%y/%H:%M')
            messages.append(line)

    for item in messages:
        Shoutbox(item[0], item[1], item[2])


def create_codecoolers_objects(codecoolers_list):
    '''
    Create codecoolers objects
    '''

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


def export_submissions():
    '''
    Exports submission data to file
    '''

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
    '''
    Exports assingments data to file
    '''

    with open('csv_databases/assingments.csv', 'w') as file:

        writer = csv.writer(file, delimiter='|')
        for assingment in Assingment.assingments:
            writer.writerow([assingment.title,
                             assingment.content,
                             assingment.date.strftime('%d.%m.%Y'),
                             str(assingment.max_grade)])


def export_codecoolers(codecoolers):
    '''
    Exports codecoolers data to file
    '''

    with open('csv_databases/codecoolers_list.csv', 'w') as file:

        writer = csv.writer(file, delimiter='|')
        for codecooler in codecoolers:
            writer.writerow([codecooler.login,
                            codecooler.password,
                            codecooler.name,
                            codecooler.surname,
                            codecooler.__class__.__name__])


def export_attendances():
    '''
    Exports attendance data to file
    '''

    with open('csv_databases/attendances.csv', 'w') as file:
        writer = csv.writer(file, delimiter='|')

        for attendance in Attendance.attendances:
            writer.writerow([attendance.student_login,
                             str(attendance.value),
                             attendance.date.strftime('%d.%m.%Y')])


def export_shoutbox_messages():
    '''
    Exports shoutbox_messages data to file
    '''

    with open('csv_databases/shoutbox.csv', 'w') as file:

        writer = csv.writer(file, delimiter='|')
        for message in Shoutbox.messages:
            writer.writerow([message.date.strftime('%d.%m.%y/%H:%M'),
                             message.author,
                             message.message])


def export_events():
    '''
    Exports events data to file
    '''

    with open('csv_databases/events.csv', 'w') as file:
        writer = csv.writer(file, delimiter='|')

        for event in Event.events:
            if event.ev_type != 'Assingment':
                writer.writerow([event.name,
                                 event.date.strftime('%d.%m.%Y'),
                                 event.login,
                                 event.ev_type])

def load_PM():
    '''
    Loads PM data from file
    '''

    with open('csv_databases/PM.csv', 'r') as file:
        reader = csv.reader(file, delimiter='|')

        messages = []

        for line in reader:
            line[0] = datetime.datetime.strptime(line[0], '%d.%m.%y/%H:%M')
            messages.append(line)

    for item in messages:
        PM(item[0], item[1], item[2], item[3])

def export_PM():
    '''
    Exports PM data to file
    '''

    with open('csv_databases/PM.csv', 'w') as file:

        writer = csv.writer(file, delimiter='|')
        for message in PM.messages:
            writer.writerow([message.date.strftime('%d.%m.%y/%H:%M'),
                             message.author,
                             message.receiver,
                             message.message])
