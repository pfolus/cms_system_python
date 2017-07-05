def greet(user):
    print('Hey {}!'.format(user.name))


def show_menu():
    menu = ['1. Show my grades',
            '2. Submit assingment',
            '0. Log out']
    for line in menu:
        print(line)


def choose_function():
    '''
    Asks an user for a number, representing function,
    and returns it
    '''
    DEFAULT_VALUE = 0
    choice = DEFAULT_VALUE
    possible_choices = [0, 1, 2]

    while choice not in possible_choices:
        try:
            choice = int(input('Choose function: '))
        except ValueError:
            print('Wrong choice.')

    return choice
