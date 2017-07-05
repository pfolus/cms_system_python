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

    options = {1: how_mentors(canvas.mentors),
               2: pass,
               3: pass,
               4: pass,
               5: show_students_list(canvas.students),
               6: show_students_with_details(canvas)}

    for option, function in options.items():
        if int(user_input) == option:
            function
