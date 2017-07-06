from models.employee_model import Employee
from models.codecooler_model import Codecooler

class Mentor(Employee):

    def __init__(self, login, password, name, surname):
        super().__init__(login, password, name, surname)