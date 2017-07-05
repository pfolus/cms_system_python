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
    '''
    Runs appropriate functions, based on user choice.

    Paramaters
    ----------
    user_input = int
    canvas = obj of Canvas class
    user = obj of Codecooler class
    '''
    if user_input == 1:
        show_grades(canvas.grades)
    elif user_input == 2:
        number = show_assingments(canvas.assingments)
        chosen_assingment = choose_assingment(number, canvas.assingments)
        check_if_submitted(chosen_assingment.title, canvas.submissions, user.login)
        is_graded = check_if_graded()
        if not is_graded:
            new_sub = add_submission(chosen_assingment, user)
            add_new_sub_to_list(canvas, new_sub)
            info_submission_added()

    return user_input


def show_grades(grades):
    pass


def choose_assingment(number, assingments):
    '''
    Asks user to choose on of possible
    assingment and returns it.

    Paramaters
    ----------
    number = int
    assingments = list (assingments from Canvas)

    Returns
    -------
    name_of_assingment = str
    '''
    choice = ''
    possible_choices = range(0, len(assingments))

    while choice not in possible_choices:

        try:
            choice = get_assingment_number()
        except ValueError:
            error_number()

    chosen_assingment = assingments[choice]

    return chosen_assingment


def check_if_submitted(assingment_name, submissions, user_login):
    '''
    Based on provided assingment name, checks if Student
    already sent a submission for it and prints info about
    it, if he did.

    Paramaters
    ----------
    assingment_name = str (title of assingment)
    submissions = list (submissions from Canvas)
    user_login = str

    Returns
    -------
    None
    '''
    for submission in submissions:
        if submission.title == assingment_name and submission.user_login == user_login:
            show_sub(submission)
            print_assingment_done()


def add_submission(assingment, user):
    '''
    Adds new submission from Student, for chosen
    assingment.

    Paramaters
    ----------
    assingment = obj of Assingment class
    user = obj of Codecooler class

    Returns
    -------
    new_sub = obj of Submission class
    '''
    answer = get_answer()
    new_sub = Submission(user.login, assingment.title, answer)

    return new_sub


def add_new_sub_to_list(canvas, submission):
    '''
    Adds new submission to the list of submissions
    in canvas object.

    Paramaters
    ----------
    canvas = obj of Canvas class
    submission = obj of Submission class

    Returns
    -------
    None
    '''
    canvas.submissions.append(submission)
