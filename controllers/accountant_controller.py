from views.accountant_view import *
from views.codecooler_view import *
from views.employee_view import *


def start_controller(canvas, user):
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
    exit = 0
    greet(user)
    choice = ''

    while choice != exit:
        show_menu()
        choice = choose_function()

        if choice == 1:
            show_students_list(canvas.students)
        elif choice == 2:
            show_students_list_detailed(canvas)
