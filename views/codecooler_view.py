from views.bcolors import Bcolors


def greet(user):
    '''
    Prints welocme message with logged user's name
    '''

    print(Bcolors.RED + Bcolors.BOLD + "\nHello " + user.name + "!\n" + Bcolors.ENDC)
