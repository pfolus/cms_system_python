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
    '''
    Welcomes user, shows menu and asks
    to choose a function, then runs specific process

    Paramaters
    ----------
    canvas = obj of Canvas class
    user = obj of Codecooler class

    Returns
    -------
    None
    '''

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
    '''
    asks for login, password, name and surname, and
    then creates a student object and adds it to 
    canvas.students list

    Paramaters
    ----------
    canvas = obj of Canvas class

    Returns
    -------
    None
    '''
    login = get_login()
    password = get_password()
    name = get_name()
    surname = get_surname()

    canvas.students.append(Student(login, password, name, surname))
    print_done()


def remove_student(canvas):
    '''
    shows student logins as a list, then asks for login until 
    correct login provided (existing), and removes proper
    student from students list. Finally prints done message.

    Paramaters
    ----------
    canvas = obj of Canvas class

    Returns
    -------
    None
    '''
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
    '''
    iterates through students list, and returns 
    True if student exists.

    Paramaters
    ----------
    login = attribute (.login) of Student class
    canvas = obj of Canvas class

    Returns
    -------
    login_exist = True or False
    '''
    login_exist = False
    for item in canvas.students:
        if item.login == login:
            login_exist = True

    return login_exist


def add_assingment(canvas):
    '''
    ask for title, content, date and max_grade, and then
    creates assingment and adds it to assingments list.

    Paramaters
    ----------
    canvas = obj of Canvas class

    Returns
    ----------
    None
    '''
    title = get_string('title')
    content = get_string('content')
    date = get_date()
    max_grade = get_int('Enter max grade: ')

    canvas.assingments.append(Assingment(title, content, date, max_grade))
    print_done()


def grade_assingment(canvas):
    '''
    Shows submissions list, asks for submission title,
    prints chosen submissions content and ask for grade.
    Checks if grade is in correct form.

    Paramaters
    ----------
    canvas = obj of Canvas class

    Returns
    -------
    None
    '''
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
    '''
    iterate through assigments and search for assigment
    with the same title as submission, and returns its 
    max_grade parameter.

    Paramaters
    ----------
    canvas = obj of Canvas class
    submission = obj of Submission class

    Returns
    -------
    item.max_grade = attribute of Assingment class
    '''

    for item in canvas.assingments:
        if item.title == submission.title:
            return item.max_grade

def check_attendance(canvas):
    '''
    iterate through students, and for each student:
    prints its full name, submenu and asks to choose
    if we want to insert absence, presence or late.

    Paramaters
    ----------
    canvas = obj of Canvas class

    Returns
    -------
    None
    '''

    index = 1
    for student in canvas.students:

        choice = ''
        while choice not in ['1','2','3']:
            print('\nStudent name:\n\n{}. {} {}'.format(index, student.name, student.surname))
            print_attendance_menu()
            choice = get_choice()
            if choice == '1':
                insert_absence(canvas.attendances, student.login)
            elif choice == '2':
                insert_late(canvas.attendances, student.login)
            elif choice == '3':
                insert_presence(canvas.attendances, student.login)
            elif choice not in ['1','2','3']:
                print_bad_choice()
        index += 1
    print_done()












