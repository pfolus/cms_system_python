from datetime import datetime


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
    index = 1
    print()
    for student in students:
        print('({}) {} {}'.format(index, student.name, student.surname))
        index += 1
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
    print()

    for student in list_to_print:

        print('({}) {} {}, Score: {}/{}, Attendance: {}%'.format(student[0],
                                                                 student[1],
                                                                 student[2],
                                                                 student[3],
                                                                 student[4],
                                                                 student[5]))

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
