from views.manager_view import *
from models.mentor_model import Mentor


def start_controller(canvas, user):

    option = ""
    greet(user)

    while option != "0":
        print_menu()
        try:
            option = ask_for_option()
            choose_option(option, canvas, user)
        except KeyError:
            option_error()


def choose_option(user_input, canvas, user):

    if user_input == "1":
        show_mentors(canvas.mentors)
    elif user_input == "2":
        show_mentors_with_details(canvas.mentors)
    elif user_input == "3":
        add_mentor(canvas.mentors)
    elif user_input == "4":
        remove_mentor(canvas.mentors)
    elif user_input == "5":
        show_students_list(canvas.students)
    elif user_input == "6":
        show_students_list_detailed(canvas)
    elif user_input == "0":
        return user_input
    else:
        raise KeyError


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
