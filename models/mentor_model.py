from models.employee_model import Employee
from models.codecooler_model import Codecooler


class Mentor(Employee):

    mentors = []

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
        Mentor.add_to_list(self)

    @classmethod
    def add_to_list(cls, object):
        cls.mentors.append(object)

    @classmethod
    def remove_mentor(cls, index):
        del cls.mentors[index]
