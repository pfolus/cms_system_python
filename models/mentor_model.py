from models.employee_model import Employee
from models.codecooler_model import Codecooler

class Mentor(Employee):

    def __init__(self, login, password, name, surname):
        '''
        Initializes Mentor instance

        Args:
            login - string
            password - string
            name - string
            surname - string
        '''
        super().__init__(login, password, name, surname)
