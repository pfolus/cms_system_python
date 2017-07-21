from prettytable import PrettyTable
from views.bcolors import Bcolors
from models.event_model import Event


def print_numbered_event(counter, event):
    '''
    Prints event with the number, next to it
    '''
    print('{}. {}'.format(counter, event))


def print_calendar_header():
    '''
    Prints header
    '''
    print('Upcoming events:\n')


def print_calendar_table(events):
    '''
    Prints upcoming events in form of a table

    Paramaters
    ----------
    events = list of Event objects

    Returns
    -------
    None
    '''
    table = PrettyTable(['', 'Name', 'Date', 'Type'])
    for event in events:
        is_past = Event.check_if_passed(event[1])
        if is_past:
            event[1].name = Bcolors.RED + event[1].name + Bcolors.ENDC
            event[1].date = Bcolors.RED + str(event[1].date) + Bcolors.ENDC
            event[1].ev_type = Bcolors.RED + event[1].ev_type + Bcolors.ENDC

        table.add_row([event[0], event[1].name, event[1].date, event[1].ev_type])
    print(table)
