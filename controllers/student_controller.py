from views import student_view
from views import codecooler_view
from views import submission_view
from views import shoutbox_view
from models.submission_model import Submission
from models.assingment_model import Assingment
from controllers import codecooler_controller
import os


def start_controller(user):
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
    codecooler_view.greet(user)

    while choice != EXIT:
        student_view.show_menu()
        choice = student_view.choose_function()
        choice = run_chosen_function(choice, user)


def run_chosen_function(user_input, user):
    '''
    Runs appropriate functions, based on user choice.

    Paramaters
    ----------
    user_input = int
    canvas = obj of Canvas class
    user = obj of Codecooler class
    '''
    if user_input == 1:
        run_grades_functions(user)
    elif user_input == 2:
        run_submission_functions(user)
    elif user_input == 3:
        os.system('clear')
        shoutbox_view.show_shoutbox_panel()
        shoutbox_view.enter_message(user.login)
    elif user_input == 4:
        codecooler_controller.edit_profile(user.login)
    return user_input


def run_grades_functions(user):
    '''
    Handles flow of showing grades related functions.

    Paramaters
    ----------
    canvas = obj of Canvas class
    user = obj of Codecooler class

    Returns
    -------
    None
    '''
    grades_sum, max_grades_sum, amount_of_grades = calculate_grades(user.login)
    student_view.show_grades_info(grades_sum, max_grades_sum, amount_of_grades)


def run_submission_functions(user):
    '''
    Handles flow of sending submission related functions.

    Paramaters
    ----------
    canvas = obj of Canvas class
    user = obj of Codecooler class

    Returns
    -------
    None
    '''
    number = student_view.show_assingments(Assingment.assingments)
    chosen_assingment = choose_assingment(number)
    check_if_submitted(chosen_assingment.title, user.login)
    is_graded = check_if_graded(chosen_assingment.title, user.login)

    if not is_graded:
        add_submission(chosen_assingment, user)
        student_view.info_submission_added()


def calculate_grades(user_login):
    '''
    Basing on student's submissions calculates its sum of grades,
    and maximum amount of grades, that could have been scored.
    It also sums the number of graded submissions.

    Paramaters
    ----------
    assingments = list (Assingment objects)
    submissions = list (Submission objects)
    user_login = str

    Returns
    -------
    grades_sum = int
    max_grades_sum = int
    amount_of_grades = int
    '''
    grades_sum = 0
    max_grades_sum = 0
    amount_of_grades = 0

    for submission in Submission.submissions:
        if submission.user_login == user_login and submission.is_checked:
            grades_sum += submission.score
            amount_of_grades += 1
            for assingment in Assingment.assingments:
                if assingment.title == submission.title:
                    max_grades_sum += assingment.max_grade

    return grades_sum, max_grades_sum, amount_of_grades


def choose_assingment(number):
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
    possible_choices = range(0, len(Assingment.assingments))

    while choice not in possible_choices:

        try:
            choice = student_view.get_assingment_number()
        except ValueError:
            student_view.error_number()

    chosen_assingment = Assingment.get_assingment_by_index(choice)

    return chosen_assingment


def check_if_submitted(assingment_name, user_login):
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
    boolean = returns False if submission for this assingment
    wasn't sent by this Student yes, otherwise returns True.
    '''
    for submission in Submission.submissions:
        if submission.title == assingment_name and submission.user_login == user_login:
            student_view.print_assingment_done()
            submission_view.show_sub(submission)


def check_if_graded(assingment_name, user_name):
    '''
    Returns True if submission was already graded, otherwise returns False
    '''
    for submission in Submission.submissions:
        if submission.title == assingment_name and user_name == submission.user_login and submission.is_checked:
            return True
        elif submission.title == assingment_name and user_name == submission.user_login and not submission.is_checked:
            return False


def add_submission(assingment, user):
    '''
    Adds new submission from Student, for chosen
    assingment.

    Paramaters
    ----------
    assingment = obj of Assingment class
    submissions = list (of Submission objects from Canvas)
    user = obj of Codecooler class

    Returns
    -------
    new_sub = obj of Submission class
    '''
    answer = student_view.get_answer()
    for submission in Submission.submissions:
        if assingment.title == submission.title and user.login == submission.user_login:
            Submission.submissions.remove(submission)

    Submission(user.login, assingment.title, answer)


def count_average_attendance(attendances_list):

    avg_att = 0
    counter = 0

    for attendance in attendances_list:

        avg_att += attendance.value
        counter += 1

    if counter > 0:
        return avg_att / counter * 100
    else:
        return avg_att
