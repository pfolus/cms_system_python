from models.codecooler_model import Codecooler


class Accountant(Codecooler):
    def __init__(self, login, password, name, surname):
        super().__init__(login, password, name, surname)
