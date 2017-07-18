from models.canvas_model import Canvas
from views import canvas_view
from controllers import manager_controller
from controllers import student_controller
from controllers import accountant_controller
from controllers import mentor_controller
from controllers import data_manager_controller


def start_controller():
    canvas = Canvas()
    try:
        data_manager_controller.load_codecoolers_list_csv(canvas)
        data_manager_controller.load_assingments_list_csv(canvas)
        data_manager_controller.load_submissions_list_csv(canvas)
        data_manager_controller.load_attendances_list_csv(canvas)
    except FileNotFoundError:
        canvas_view.print_file_not_found_error()
        return False
    canvas_view.show_login_menu()
    logged_in = False
    while not logged_in:
        user, logged_in = login(canvas)
    run_controller(user, canvas)
    data_manager_controller.export_data_to_csv(canvas)


def login(canvas):

    login = canvas_view.get_login()
    password = canvas_view.get_password()

    LOGIN_INDEX = 0
    PASSWORD_INDEX = 1

    summary_list = canvas.mentors + canvas.managers + canvas.students + canvas.accountants

    for user in summary_list:
        if user.login == login and user.password == password:
            return user, True

    canvas_view.wrong_user()
    return None, False


def run_controller(user, canvas):

    class_name = user.__class__.__name__

    if class_name == 'Student':
        student_controller.start_controller(canvas, user)
    if class_name == 'Mentor':
        mentor_controller.start_controller(canvas, user)
    if class_name == 'Accountant':
        accountant_controller.start_controller(canvas, user)
    if class_name == 'Manager':
        manager_controller.start_controller(canvas, user)
