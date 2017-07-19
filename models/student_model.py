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

    @classmethod
    def check_if_login_exists(cls, login):
        '''
        iterates through students list, and returns
        True if student exists.

        Paramaters
        ----------
        login = attribute (.login) of Student class

        Returns
        -------
        login_exist = True or False
        '''
        login_exist = False

        for item in cls.students:
            if item.login == login:
                login_exist = True

        return login_exist

    @classmethod
    def remove_student(cls, login):
        for student in cls.students:
            if student.login == login:
                cls.students.remove(student)
