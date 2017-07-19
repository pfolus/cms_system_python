from models.student_model import Student
from models.assingment_model import Assingment
from models.event_model import Event
from views import event_view


def create_calendar(login):
    is_student = Student.check_if_login_exists(login)
    if is_student:
        fill_student_calendar(login)


def fill_student_calendar(login):
    coming_assingments = Assingment.get_coming_assingments()
    for assingment in coming_assingments:
        Event(assingment.title, assingment.date, login, 'Assingment')
