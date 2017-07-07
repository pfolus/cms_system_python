from models.codecooler_model import Codecooler


class Manager(Codecooler):
    '''
    Initializes Manager instance

    Args:
        strings
    '''

    def __init__(self, login, password, name, surname):
        super().__init__(login, password, name, surname)
