from models.employee_model import Employee


class Accountant(Employee):
    def __init__(self, login, password, name, surname):
        super().__init__(login, password, name, surname)
