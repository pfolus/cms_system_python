def print_menu():
    '''
    Prints manager submenu
    '''

    print('''1. List mentors
2. List mentors with details
3. Add mentor
4. Remove mentor
5. List students
6. List students with details
7. Shoutbox message
8. Change password
9. Add an event
10. Show upcoming events
11. Remove an event
12. Private messages
0. Log out
''')


def ask_for_option():
    '''
    Get user inputfor choosing option in menu

    Returns:
        string
    '''

    return input("Choose option: ")


def option_error():
    '''
    Print error message
    '''

    print("There isn't such option!")


def show_mentors_with_details(mentors):
    '''
    Prints all mentors' details

    Args:
        mentors - list with objects
    '''

    index = 1
    print()
    for mentor in mentors:
        print("({}) {} {} - {}".format(index, mentor.name,
                                      mentor.surname, mentor.login))
        index += 1
    print()


def show_mentors(mentors):
    '''
    Prints all mentors

    Args:
        mentors - list with objects
    '''

    index = 1
    print()
    for mentor in mentors:
        print("({}) {} {}".format(index, mentor.name, mentor.surname))
        index += 1
    print()


def ask_for_index():
    '''
    Gets index input from user and convert it to int

    Rturns:
        int
    '''

    is_correct = False

    while not is_correct:
        try:
            index = int(input("Enter index: "))
            if index < 1:
                option_error()
            else:
                is_correct = True
        except ValueError:
            option_error()

    return index - 1
