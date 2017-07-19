from operator import attrgetter
from models.event_model import Event


def show_calendar(login):
    print('Upcoming events:\n')
    events = Event.events[:]
    events.sort(key=attrgetter('date'))

    events_to_print = []
    for event in events:
        if event.login == login or event.login == 'all':
            events_to_print.append(event)

    if len(events_to_print) > 10:
        for event in events_to_print[-10:-1]:
            print(event)

    else:
        for event in events_to_print:
            print(event)
    print()
