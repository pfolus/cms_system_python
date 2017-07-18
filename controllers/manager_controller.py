from views import manager_view
from views import codecooler_view
from views import employee_view
from models.mentor_model import Mentor


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

    option = ""
    codecooler_view.greet(user)

    while option != "0":
        manager_view.print_menu()
        try:
            option = manager_view.ask_for_option()
            choose_option(option, canvas, user)
        except KeyError:
            manager_view.option_error()


def choose_option(user_input, canvas, user):
    '''
    Runs appropriate functions, based on user choice.

    Paramaters
    ----------
    user_input = int
    canvas = obj of Canvas class
    user = obj of Codecooler class
    '''

    if user_input == "1":
        manager_view.show_mentors(canvas.mentors)
    elif user_input == "2":
        manager_view.show_mentors_with_details(canvas.mentors)
    elif user_input == "3":
        add_mentor(canvas.mentors)
    elif user_input == "4":
        remove_mentor(canvas.mentors)
    elif user_input == "5":
        employee_view.show_students_list(canvas.students)
    elif user_input == "6":
        employee_view.show_students_list_detailed(canvas)
    elif user_input == "0":
        return user_input
    else:
        raise KeyError


def add_mentor(mentors):
    '''
    Takes user_inputs and appends mentors list with Mentor object
    '''

    login = manager_view.ask_login()
    password = manager_view.ask_password()
    name = manager_view.ask_name()
    surname = manager_view.ask_surname()

    mentors.append(Mentor(login, password, name, surname))


def remove_mentor(mentors):
    '''
    Removes mentor instance with index entered by user from mentors list
    '''

    manager_view.show_mentors(mentors)

    try:
        index = manager_view.ask_for_index()
        del mentors[index]
    except IndexError:
        manager_view.option_error()
