from models.mentor_model import Mentor
from views.mentor_view import *
from models.student_model import Student

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
            check_assingment()
        elif choice == '5':
            remove_assingment()
        elif choice == '6':
            add_student()
        elif choice != '0':
            print_bad_choice()


def add_student():

    login = get_login()
    password = get_password()
    name = get_name()
    surname = get_surname()

    Student(login, password, name, surname)

def add_assignment():

    pass


def grade_assingment():
    pass


def check_assingment():
    pass


def remove_assingment():
    pass





