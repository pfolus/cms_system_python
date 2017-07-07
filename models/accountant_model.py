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
    def __init__(self, login, password, name, surname):
        super().__init__(login, password, name, surname)
