from views.student_view import *
from model.canvas_model import Canvas


def start_controller(canvas, user):
    choice = ''
    EXIT = 0
    greet(user)

    while choice != EXIT:
        show_menu()
        choice = choose_function()
        choice = run_chosen_function(choice, canvas, user)


def run_chosen_function(user_input, canvas, user):

    if user_input == 1:
        show_grades(canvas.grades)
    elif user_input == 2:
        number = show_assingments(canvas.assingments)
        chosen_assingment = choose_assingment(number, canvas.assingments)
    elif user_input == 0:
        return user_input


def show_grades(grades):
    pass


def choose_assingment(number, assingments):
    choice = ''
    possible_choices = range(0, len)

    while choice not in possible_choices:

        try:
            choice = int(input("Choose assingment: "))
        except ValueError:
            print('Wrong number.')
    return assingments[choice]
