from models.manager_model import Manager
from models.student_model import Student
from models.mentor_model import Mentor
from models.accountant_model import Accountant
from views import canvas_view
from controllers import manager_controller
from controllers import student_controller
from controllers import accountant_controller
from controllers import mentor_controller
from controllers import data_manager_controller


def start_controller():

    try:
        data_manager_controller.load_shoutbox_messages()
    except FileNotFoundError:
        pass
    try:
        data_manager_controller.load_data_from_csv()
    except FileNotFoundError:
        canvas_view.print_file_not_found_error()
        return False

    canvas_view.show_login_menu()

    logged_in = False
    while not logged_in:
        user, logged_in = login()

    run_controller(user)
    data_manager_controller.export_data_to_csv()


def login():

    login = canvas_view.get_login()
    password = canvas_view.get_password()

    LOGIN_INDEX = 0
    PASSWORD_INDEX = 1

    summary_list = Mentor.mentors + Manager.managers + Student.students + Accountant.accountants

    for user in summary_list:
        if user.login == login and user.password == password:
            return user, True

    canvas_view.wrong_user()

    return None, False


def run_controller(user):

    class_name = user.__class__.__name__

    if class_name == 'Student':
        student_controller.start_controller(user)
    if class_name == 'Mentor':
        mentor_controller.start_controller(user)
    if class_name == 'Accountant':
        accountant_controller.start_controller(user)
    if class_name == 'Manager':
        manager_controller.start_controller(user)
