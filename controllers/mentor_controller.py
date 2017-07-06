from models.mentor_model import Mentor
from views.mentor_view import *
from models.student_model import Student
from models.canvas_model import Canvas

def start_controller(canvas, user):

    print_welcome(user)
    choice = '99'


    while choice != '0':
        print_menu()
        choice = get_choice()

        if choice == '1':
            view_student_details()
        elif choice == '2':
            add_assingment()
        elif choice == '3':
            grade_assingment()
        elif choice == '4':
            check_attendance()
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


def remove_student(canvas):

    #show_student_login_list()
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


def add_assignment():

    pass


def grade_assingment():
    pass


def check_attendance():
    pass








