from models.mentor_model import Mentor
from views import mentor_view
from models.student_model import Student
from models.canvas_model import Canvas
from models.assingment_model import Assingment
from views import employee_view
from views import codecooler_view
from models.submission_model import Submission
from models.attendance_model import Attendance
from controllers import attendance_controller


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

    codecooler_view.greet(user)
    choice = '99'

    while choice != '0':
        mentor_view.print_menu()
        choice = mentor_view.get_choice()

        if choice == '1':
            employee_view.show_students_list_detailed(canvas)
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
            mentor_view.print_bad_choice()


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
    login = mentor_view.get_login()
    password = mentor_view.get_password()
    name = mentor_view.get_name()
    surname = mentor_view.get_surname()

    canvas.students.append(Student(login, password, name, surname))
    canvas.attendances.append(Attendance(login))
    mentor_view.print_done()


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
    mentor_view.show_logins(canvas)
    login = mentor_view.get_student_login()

    while not login_exist(login, canvas):
        mentor_view.print_not_exist()
        login = mentor_view.get_student_login()

    for student in canvas.students:
        if student.login == login:
            canvas.students.remove(student)
            for attendance in canvas.attendances:
                if attendance.student_login == login:
                    canvas.attendances.remove(attendance)
            mentor_view.print_done()


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
    max_grade = 0

    title = mentor_view.get_string('title')
    content = mentor_view.get_string('content')
    date = mentor_view.get_date()
    while max_grade <= 0:
        max_grade = mentor_view.get_int('Enter max grade: ')

    canvas.assingments.append(Assingment(title, content, date, max_grade))
    mentor_view.print_done()


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
    mentor_view.show_submissions(canvas)
    submission = mentor_view.get_submission(canvas)
    print('\nSubmission Answer:\n{}'.format(submission.answer))
    max_grade = max_grade_by_title(canvas, submission)

    mentor_view.print_grades_range_info(max_grade)
    grade = mentor_view.get_int('Enter submission grade: ')

    while (grade > max_grade) or (grade < -3):
        mentor_view.print_grades_range_info(max_grade)
        grade = mentor_view.get_int('Enter submission grade: ')

    submission.score = grade
    submission.is_checked = True
    mentor_view.print_done()


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
        while choice not in ['1', '2', '3']:
            mentor_view.show_numbered_student(index, student.name, student.surname)
            mentor_view.print_attendance_menu()
            choice = mentor_view.get_choice()
            if choice == '1':
                attendance_controller.insert_absence(canvas.attendances, student.login)
            elif choice == '2':
                attendance_controller.insert_late(canvas.attendances, student.login)
            elif choice == '3':
                attendance_controller.insert_presence(canvas.attendances, student.login)
            elif choice not in ['1', '2', '3']:
                mentor_view.print_bad_choice()
        index += 1
    mentor_view.print_done()
