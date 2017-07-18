from views import student_view
from views import codecooler_view
from views import submission_view
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
    codecooler_view.greet(user)

    while choice != EXIT:
        student_view.show_menu()
        choice = student_view.choose_function()
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
        run_grades_functions(canvas, user)
    elif user_input == 2:
        run_submission_functions(canvas, user)

    return user_input


def run_grades_functions(canvas, user):
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
    grades_sum, max_grades_sum, amount_of_grades = calculate_grades(canvas.assingments, canvas.submissions, user.login)
    student_view.show_grades_info(grades_sum, max_grades_sum, amount_of_grades)


def run_submission_functions(canvas, user):
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
    number = student_view.show_assingments(canvas.assingments)
    chosen_assingment = choose_assingment(number, canvas.assingments)
    check_if_submitted(chosen_assingment.title, canvas.submissions, user.login)
    is_graded = check_if_graded(chosen_assingment.title, canvas.submissions, user.login)

    if not is_graded:
        new_sub = add_submission(chosen_assingment, canvas.submissions, user)
        add_new_sub_to_list(canvas, new_sub)
        student_view.info_submission_added()


def calculate_grades(assingments, submissions, user_login):
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

    for submission in submissions:
        if submission.user_login == user_login and submission.is_checked:
            grades_sum += submission.score
            amount_of_grades += 1
            for assingment in assingments:
                if assingment.title == submission.title:
                    max_grades_sum += assingment.max_grade

    return grades_sum, max_grades_sum, amount_of_grades


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
            choice = student_view.get_assingment_number()
        except ValueError:
            student_view.error_number()

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
    boolean = returns False if submission for this assingment
    wasn't sent by this Student yes, otherwise returns True.
    '''
    for submission in submissions:
        if submission.title == assingment_name and submission.user_login == user_login:
            student_view.print_assingment_done()
            submission_view.show_sub(submission)


def check_if_graded(assingment_name, submissions, user_name):
    '''
    Returns True if submission was already graded, otherwise returns False
    '''
    for submission in submissions:
        if submission.title == assingment_name and user_name == submission.user_login and submission.is_checked:
            return True
        elif submission.title == assingment_name and user_name == submission.user_login and submission.is_checked is False:
            return False


def add_submission(assingment, submissions, user):
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
    for submission in submissions:
        if assingment.title == submission.title and user.login == submission.user_login:
            submissions.remove(submission)

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
