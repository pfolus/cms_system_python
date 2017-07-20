from views import accountant_view
from views import codecooler_view
from views import employee_view
from views import shoutbox_view
from views import event_view
from views import PM_view
from models.attendance_model import Attendance
from models.student_model import Student
from models.assingment_model import Assingment
from models.submission_model import Submission
from controllers import codecooler_controller
from controllers import employee_controller
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
    exit = 0
    codecooler_view.greet(user)
    choice = ''

    while choice != exit:
        accountant_view.show_menu()
        choice = accountant_view.choose_function()

        if choice == 1:
            employee_view.show_students_list(Student.students)
        elif choice == 2:
            employee_controller.show_students_list_detailed()
        elif choice == 4:
            codecooler_controller.edit_profile(user.login)
        elif choice == 3:
            os.system('clear')
            shoutbox_view.show_shoutbox_panel()
            shoutbox_view.enter_message(user.login)
        elif choice == 5:
            employee_controller.add_event()
        elif choice == 6:
            event_view.get_calendar(user.login)
        elif choice == 7:
            employee_controller.remove_event(user.login)
