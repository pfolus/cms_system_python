from views.manager_view import *
from models.mentor_model import Mentor


def start_controller(canvas, user):

    option = ""
    greet(user)

    while option != "0":
        print_menu()
        try:
            user_input = ask_for_option()
            choose_option(user_input, canvas, user)
        except ValueError:
            option_error()


def choose_option(user_input, canvas, user):

    options = {1: show_mentors(canvas.mentors),
               2: show_mentors_with_details(canvas.mentors),
               3: add_mentor(canvas.mentors),
               4: remove_mentor(canvas.mentors),
               5: show_students_list(canvas.students),
               6: show_students_with_details(canvas)}

    for option, function in options.items():
        if int(user_input) == option:
            function


def add_mentor(mentors):

    login = ask_login()
    password = ask_password()
    name = ask_name()
    surname = ask_surname()

    mentors.append(Mentor(login, password, name, surname))


def remove_mentor(mentors):

    show_mentors(mentors)

    try:
        index = ask_for_index()
        del mentors[index]
    except IndexError:
        option_error()
