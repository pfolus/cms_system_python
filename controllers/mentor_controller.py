from models.mentor_model import Mentor
from views.mentor_view import *
from models.student_model import Student
from models.canvas_model import Canvas
from models.assingment_model import Assingment
from views.employee_view import *
from models.submission_model import Submission
from models.attendance_model import Attendance
from controllers.attendance_controller import *

def start_controller(canvas, user):

    print_welcome(user)
    choice = '99'


    while choice != '0':
        print_menu()
        choice = get_choice()

        if choice == '1':
            show_students_list_detailed(canvas)
        elif choice == '2':
            add_assingment(canvas)
        elif choice == '3':
            grade_assingment(canvas)
        elif choice == '4':
            check_attendance(canvas)
        elif choice == '5':
            remove_student(canvas)
        elif choice == '6':
            add_student(canvas)
        elif choice != '0':
            print_bad_choice()


def add_student(canvas):

    login = get_login()
    password = get_password()
    name = get_name()
    surname = get_surname()

    canvas.students.append(Student(login, password, name, surname))
    print_done()


def remove_student(canvas):

    show_logins(canvas)
    login = get_student_login()

    while not login_exist(login, canvas):
        print_not_exist()
        login = get_student_login()

    for student in canvas.students:
        if student.login == login:
            canvas.students.remove(student)
            print_done()


def login_exist(login, canvas):

    login_exist = False
    for item in canvas.students:
        if item.login == login:
            login_exist = True

    return login_exist


def add_assingment(canvas):

    title = get_string('title')
    content = get_string('content')
    date = get_date()
    max_grade = get_int('Enter max grade: ')

    canvas.assingments.append(Assingment(title, content, date, max_grade))
    print_done()


def grade_assingment(canvas):

    show_submissions(canvas)
    submission = get_submission(canvas)
    print('\nSubmission Answer:\n{}'.format(submission.answer))

    grade = get_int('Enter submission grade: ')
    max_grade = max_grade_by_title(canvas, submission)

    while (grade > max_grade) or (grade < -3):
        print('Grade must be in range <-3:{}>'.format(max_grade))
        grade = get_int('Enter submission grade: ')

    submission.score = grade
    submission.is_checked = True
    print_done()

def max_grade_by_title(canvas, submission):

    for item in canvas.assingments:
        if item.title == submission.title:
            return item.max_grade

def check_attendance(canvas):

    for student in canvas.students:
        insert_presence(canvas.attendances, student.login)

    choice = ''
    while choice != '0':
        print_attendance_menu()
        choice = get_choice()

        if choice == '1':
            show_fullnames(canvas)
            student = get_student(canvas)
            insert_absence(canvas.attendances, student.login)
            print_done()
            
        elif choice == '2':
            show_fullnames(canvas)
            student = get_student(canvas)
            insert_late(canvas.attendances, student.login)
            print_done()

        elif choice != '0':
            print_bad_choice()













