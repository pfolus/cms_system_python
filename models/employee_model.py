from models.codecooler_model import Codecooler


class Employee(Codecooler):
    '''
    Initializes Employee instance

    Args:
        login - string
        password - string
        name - string
        surname - string
    '''

    def __init__(self, login, password, name, surname):
        super().__init__(login, password, name, surname)
