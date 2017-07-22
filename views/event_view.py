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
    print('coming events:\n')


def print_calendar_table(events):
    '''
    Prints upcoming events in form of a table

    Paramaters
    ----------
    events = list of Event objects

    Returns
    -------saa
    None
    '''
    table = PrettyTable(['', 'Name', 'Date', 'Type'])
    for event in events:
        ev_date = event[1].date
        ev_name = event[1].name
        ev_type = event[1].ev_type
        is_past2 = Event.check_if_passed(event[1])
        if is_past:
            ev_name = Bcolors.RED + event[1].name + Bcolors.ENDC
            ev_date = Bcolors.RED + str(event[1].date) + Bcolors.ENDC
            ev_type = Bcolors.RED + event[1].ev_type + Bcolors.ENDC

        table.add_row([event[0], ev_name, ev_date, ev_type])
    print(table)
