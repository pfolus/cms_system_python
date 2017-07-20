from datetime import datetime
from prettytable import PrettyTable


def show_students_list(students):
    '''
    Prints every student info in new line

    Paramaters
    ----------
    students_list = list (of Student obj)

    Returns
    -------
    None
    '''
    table = PrettyTable(['', 'Name', 'Surname'])
    index = 1
    print()
    for student in students:
        table.add_row([index, student.name, student.surname])
        index += 1
    print(table)
    print()


def print_detailed_students_list(list_to_print):
    '''
    Prints detailed info about every student in new line

    Paramaters
    ----------
    canvas = obj of Canvas class

    Returns
    -------
    None
    '''
    table = PrettyTable(['', 'Name', 'Surname', 'Score', 'Attendance'])
    print()

    for student in list_to_print:

        table.add_row([student[0], student[1], student[2],
                        '{}/{}'.format(student[3], student[4]),
                        '{}%'.format(student[5])])

    print(table)
    print()


def print_add_event():
    print('Add new event, to the calendar: ')


def get_date():
    '''
    Asks for date until date with correct format passed.
    If not, prints error message.

    Returns
    -------
    correct_date = datetime object
    '''

    while True:
        date = input('Enter date in format dd.mm.yyyy: ')
        try:
            correct_date = datetime.strptime(date, '%d.%m.%Y')
            return correct_date
        except ValueError:
            print('Wrong input!')


def get_string(item):
    return input('\nEnter {}: '.format(item))


def get_event(events):
    event_number = ''
    POSSIBLE_NUMBERS = range(1, len(events) + 1)
    while event_number not in POSSIBLE_NUMBERS:
        try:
            event_number = int(input("Choose an event: "))

        except ValueError:
            print('Wrong number.')

    return event_number - 1
