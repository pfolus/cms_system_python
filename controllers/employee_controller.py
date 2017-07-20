from views import employee_view
from views import event_view
from models.student_model import Student
from models.attendance_model import Attendance
from models.attendance_model import Attendance
from models.assingment_model import Assingment
from models.submission_model import Submission
from models.event_model import Event
from controllers import student_controller


def show_students_list_detailed():

    list_to_print = []
    index = 1

    for student in Student.students:

        attendances = Attendance.get_student_attendances(student.login)
        avg_att = student_controller.count_average_attendance(attendances)

        [grades_sum,
         max_grades_sum,
         amount_of_grades] = student_controller.calculate_grades(student.login)

        list_to_print.append([index, student.name, student.surname,
                              grades_sum, max_grades_sum, avg_att])

        index += 1

    employee_view.print_detailed_students_list(list_to_print)


def add_event():
    employee_view.print_add_event()
    title = employee_view.get_string('title')
    date = employee_view.get_date()

    Event(title, date)


def remove_event(login):
    events = event_controller.get_calendar(login)
    event_index = employee_view.get_event(events)
    Event.remove_event(events[event_index])
