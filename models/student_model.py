from models.codecooler_model import Codecooler


class Student(Codecooler):

    students = []

    def __init__(self, login, password, name, surname):
        '''
        Initializes Student instance

        Args:
            login - string
            password - string
            name - string
            surname - string
        '''
        super().__init__(login, password, name, surname)
        Student.add_to_list(self)

    @classmethod
    def add_to_list(cls, object):
        cls.students.append(object)
