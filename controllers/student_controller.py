from views.student_view import *


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
        show_mentors_with_details(canvas.mentors)
    elif user_input == 0:
        return user_input


def show_grades(grades):
    pass


def submit_assingment(assingments, submissions):
    pass
