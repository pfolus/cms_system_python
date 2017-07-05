from views.student_view import *
from views.submission_view import *
from models.canvas_model import Canvas
from models.submission_model import Submission


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
        check_if_submitted(chosen_assingment.title, canvas.submissions, user.login)
        add_submission(chosen_assingment, user)

    elif user_input == 0:
        return user_input


def show_grades(grades):
    pass


def choose_assingment(number, assingments):
    '''
    Returns
    ------
    name_of_assingment = str
    '''
    choice = ''
    possible_choices = range(0, len)

    while choice not in possible_choices:

        try:
            choice = get_assingment_number()
        except ValueError:
            error_number()

    chosen_assingment = assingments[choice]

    return chosen_assingment


def check_if_submitted(assingment_name, submissions, user_login):
    '''
    Paramaters
    ----------
    assingment = str (title of assingment)
    '''
    for submission in submissions:
        if submission.title == assingment_name and submission.user_login == user_login:
            show_sub(submission)
            print_assingment_done()


def add_submission(assingment, user):
    answer = get_answer()
    new_sub = Submission(user.login, assingment.title, answer)
