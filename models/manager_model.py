from models.codecooler_model import Codecooler


class Manager(Codecooler):

    managers = []

    '''
    Initializes Manager instance

    Args:
        strings
    '''

    def __init__(self, login, password, name, surname):
        super().__init__(login, password, name, surname)
        Manager.add_to_list(self)

    @classmethod
    def add_to_list(cls, object):
        cls.managers.append(object)
