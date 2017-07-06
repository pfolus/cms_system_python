from views.accountant_view import *
from views.employee_view import *


def start_controller(canvas, user):
    exit = 0
    greet(user)
    choice = ''

    while choice != exit:
        show_menu()
        choice = choose_function()

        if choice == 1:
            show_students_list(canvas.students)
