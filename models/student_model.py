from models.codecooler_model import Codecooler


class Student(Codecooler):

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
