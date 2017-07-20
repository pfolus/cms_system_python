from operator import attrgetter
from models.event_model import Event


def get_calendar(login):
    print('Upcoming events:\n')
    events = Event.events[:]
    events.sort(key=attrgetter('date'))

    events_to_print = []
    for event in events:
        if event.login == login or event.login == 'all':
            events_to_print.append(event)
    counter = 1

    if len(events_to_print) > 10:
        for event in events_to_print[-11:-1]:
            print('{}. {}'.format(counter, event))
            counter += 1
    else:
        for event in events_to_print:
            print('{}. {}'.format(counter, event))
            counter += 1
    print()

    return events_to_print
