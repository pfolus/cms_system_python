from models.student_model import Student
from models.assingment_model import Assingment
from models.event_model import Event
from views import event_view
from operator import attrgetter


def create_calendar(login):
    is_student = Student.check_if_login_exists(login)
    if is_student:
        fill_student_calendar(login)


def fill_student_calendar(login):
    coming_assingments = Assingment.get_coming_assingments()
    for assingment in coming_assingments:
        Event(assingment.title, assingment.date, login, 'Assingment')


def get_calendar(login):
    event_view.print_calendar_header()
    events = Event.events[:]
    events.sort(key=attrgetter('date'))

    temp_list = []
    for event in events:
        if event.login == login or event.login == 'all':
            temp_list.append(event)
    counter = 1

    events_to_print = []

    if len(temp_list) > 10:
        for event in temp_list[-11:-1]:
            events_to_print.append([counter, event])
            counter += 1
    else:
        for event in temp_list:
            events_to_print.append([counter, event])
            counter += 1

    event_view.print_calendar_table(events_to_print)
