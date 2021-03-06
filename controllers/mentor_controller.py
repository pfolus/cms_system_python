import os
from datetime import datetime
from models.mentor_model import Mentor
from models.student_model import Student
from models.assingment_model import Assingment
from models.submission_model import Submission
from models.attendance_model import Attendance
from models.private_messages_model import PM
from views import mentor_view
from views import employee_view
from views import codecooler_view
from views import shoutbox_view
from views import event_view
from views import PM_view
from controllers import attendance_controller
from controllers import event_controller
from controllers import codecooler_controller
from controllers import employee_controller


def start_controller(user):
    '''
    Welcomes user, shows menu and asks
    to choose a function, then runs specific process

    Paramaters
    ----------
    None
    user = obj of Codecooler class

    Returns
    -------
    None
    '''

    codecooler_view.greet(user)
    choice = '99'

    while choice != '0':
        mentor_view.print_menu()
        choice = mentor_view.get_choice()

        if choice == '1':
            employee_controller.show_students_list_detailed()
        elif choice == '2':
            add_assingment()
        elif choice == '3':
            grade_assingment()
        elif choice == '4':
            check_attendance()
        elif choice == '5':
            remove_student()
        elif choice == '6':
            add_student()
        elif choice == '7':
            os.system('clear')
            shoutbox_view.show_shoutbox_panel()
            shoutbox_view.enter_message(user.login)
        elif choice == '8':
            codecooler_controller.edit_profile(user.login)
        elif choice == '9':
            employee_controller.add_event()
        elif choice == '10':
            event_controller.get_calendar(user.login)
        elif choice == '11':
            employee_controller.remove_event(user.login)
        elif choice == '12':
            os.system('clear')
            codecooler_controller.show_logins()
            receiver = codecooler_controller.get_correct_login()
            os.system('clear')
            PM_view.show_PM_panel(user.login, receiver)
            PM_view.enter_message(user.login, receiver)
        elif choice != '0':
            mentor_view.print_bad_choice()


def add_student():
    '''
    asks for login, password, name and surname, and
    then creates a student object and adds it to
    students list

    Paramaters
    ----------

    Returns
    -------
    None
    '''
    login = codecooler_view.ask_login()
    password = codecooler_view.ask_password()
    name = codecooler_view.ask_name()
    surname = codecooler_view.ask_surname()

    Student(login, password, name, surname)
    mentor_view.print_done()


def remove_student():
    '''
    shows student logins as a list, then asks for login until
    correct login provided (existing), and removes proper
    student from students list. Finally prints done message.

    Paramaters
    ----------
    None

    Returns
    -------
    None
    '''
    mentor_view.show_logins()
    get_correct_login()
    Student.remove_student(login)

    for attendance in Attendance.attendances:
        if attendance.student_login == login:
            Attendance.attendances.remove(attendance)
    mentor_view.print_done()


def get_correct_login():
    login = mentor_view.get_student_login()

    while not Student.check_if_login_exists(login):
        mentor_view.print_not_exist()
        login = mentor_view.get_student_login()
    return login


def add_assingment():
    '''
    ask for title, content, date and max_grade, and then
    creates assingment and adds it to assingments list.

    Paramaters
    ----------
    None

    Returns
    ----------
    None
    '''
    max_grade = 0

    title = mentor_view.get_string('title')
    content = mentor_view.get_string('content')
    date = mentor_view.get_date()
    while max_grade <= 0:
        max_grade = mentor_view.get_int('Enter max grade: ')

    Assingment(title, content, date, max_grade)
    mentor_view.print_done()


def grade_assingment():
    '''
    Shows submissions list, asks for submission title,
    prints chosen submissions content and ask for grade.
    Checks if grade is in correct form.

    Paramaters
    ----------
    None

    Returns
    -------
    None
    '''
    mentor_view.show_submissions()
    submission = mentor_view.get_submission()
    print('\nSubmission Answer:\n{}'.format(submission.answer))
    max_grade = max_grade_by_title(submission)

    mentor_view.print_grades_range_info(max_grade)
    grade = mentor_view.get_int('Enter submission grade: ')

    while (grade > max_grade) or (grade < -3):
        mentor_view.print_grades_range_info(max_grade)
        grade = mentor_view.get_int('Enter submission grade: ')

    submission.score = grade
    submission.is_checked = True
    mentor_view.print_done()


def max_grade_by_title(submission):
    '''
    iterate through assigments and search for assigment
    with the same title as submission, and returns its
    max_grade parameter.

    Paramaters
    ----------
    submission = obj of Submission class

    Returns
    -------
    item.max_grade = attribute of Assingment class
    '''

    for item in Assingment.assingments:
        if item.title == submission.title:
            return item.max_grade


def check_attendance():
    '''
    iterate through students, and for each student:
    prints its full name, submenu and asks to choose
    if we want to insert absence, presence or late.

    Paramaters
    ----------
    None

    Returns
    -------
    None
    '''

    index = 1

    for student in Student.students:

        attendance_dates = [att.date for att in Attendance.get_student_attendances(student.login)]

        if datetime.today().date() in attendance_dates and Attendance.get_student_attendance_by_date(student.login, datetime.today().date()).value == 0:

            mentor_view.show_numbered_student(index, student.name, student.surname)
            choice = ''

            while choice not in ['y', 'n']:

                choice = mentor_view.ask_for_late()

                if choice == 'y':
                    att = Attendance.get_student_attendance_by_date(student.login, datetime.today().date())
                    att.value = 0.8

        elif datetime.today().date() not in attendance_dates:

            mentor_view.show_numbered_student(index, student.name, student.surname)
            choice = ''

            while choice not in ['1', '2', '3']:

                mentor_view.print_attendance_menu()
                choice = mentor_view.get_choice()

                if choice == '1':
                    Attendance(student.login, 1.0)

                elif choice == '2':
                    Attendance(student.login, 0.8)

                elif choice == '3':
                    Attendance(student.login, 0)

                elif choice not in ['1', '2', '3']:
                    mentor_view.print_bad_choice()

        index += 1

    mentor_view.attendance_checked()
