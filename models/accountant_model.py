from models.employee_model import Employee


class Accountant(Employee):
    '''
    Initializes Accountant instance

    Args:
        login - string
        password - string
        name - string
        surname - string
    '''

    accountants = []

    def __init__(self, login, password, name, surname):
        super().__init__(login, password, name, surname)
        Accountant.add_to_list(self)

    @classmethod
    def add_to_list(cls, object):
        cls.accountants.append(object)
