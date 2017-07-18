from models.codecooler_model import Codecooler


class Employee(Codecooler):

    employees = []

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
        Employee.add_to_list(self)

    @classmethod
    def add_to_list(cls, object):
        cls.employees.append(object)
