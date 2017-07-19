from views import manager_view
from views import codecooler_view
from views import employee_view
from views import shoutbox_view
from models.mentor_model import Mentor
from models.student_model import Student
from models.attendance_model import Attendance
from models.assingment_model import Assingment
from models.submission_model import Submission
from controllers import employee_controller
import os


def start_controller(user):
    '''
    Welcomes user, shows menu and asks
    to choose a function

    Paramaters
    ----------
    canvas = obj of Canvas class
    user = obj of Codecooler class

    Returns
    -------
    None
    '''

    option = ""
    codecooler_view.greet(user)

    while option != "0":
        manager_view.print_menu()
        try:
            option = manager_view.ask_for_option()
            choose_option(option, user)
        except KeyError:
            manager_view.option_error()


def choose_option(user_input, user):
    '''
    Runs appropriate functions, based on user choice.

    Paramaters
    ----------
    user_input = int
    canvas = obj of Canvas class
    user = obj of Codecooler class
    '''

    if user_input == "1":
        manager_view.show_mentors(Mentor.mentors)
    elif user_input == "2":
        manager_view.show_mentors_with_details(Mentor.mentors)
    elif user_input == "3":
        add_mentor()
    elif user_input == "4":
        remove_mentor()
    elif user_input == "5":
        employee_view.show_students_list(Student.students)
    elif user_input == "6":
        employee_controller.show_students_list_detailed()
    elif user_input == "7":
            os.system('clear')
            shoutbox_view.show_shoutbox_panel()
            shoutbox_view.enter_message(user.login)
    elif user_input == "0":
        return user_input
    else:
        raise KeyError


def add_mentor():
    '''
    Takes user_inputs and appends mentors list with Mentor object
    '''

    login = codecooler_view.ask_login()
    password = codecooler_view.ask_password()
    name = codecooler_view.ask_name()
    surname = codecooler_view.ask_surname()

    Mentor(login, password, name, surname)


def remove_mentor():
    '''
    Removes mentor instance with index entered by user from mentors list
    '''

    manager_view.show_mentors(Mentor.mentors)

    try:
        index = manager_view.ask_for_index()
        Mentor.remove_mentor(index)
    except IndexError:
        manager_view.option_error()
