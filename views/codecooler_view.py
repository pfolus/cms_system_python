from views.bcolors import Bcolors


def greet(user):

    print(Bcolors.RED + Bcolors.BOLD + "\nHello " + user.name + "!\n" + Bcolors.ENDC)
