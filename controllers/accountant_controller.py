from views import accountant_view
from views import codecooler_view
from views import employee_view
from models.attendance_model import Attendance
from models.student_model import Student
from models.assingment_model import Assingment
from models.submission_model import Submission
from controllers import codecooler_controller


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
            employee_view.show_students_list_detailed(Student.students, Attendance.attendances, Assingment.assingments, Submission.submissions)
        elif choice == 3:
            codecooler_controller.edit_profile(user.login)
