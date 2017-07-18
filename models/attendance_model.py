from datetime import datetime


class Attendance:

    attendances = []

    def __init__(self, student_login, value):
        '''
        Initializes Attendance object

        Args:
            student_login - string
            value - float
            date - datetime object
        '''
        self.student_login = student_login
        self.value = value
        self.date = datetime.today()
        Attendance.add_to_list(self)

    @classmethod
    def add_to_list(cls, object):
        cls.attendances.append(object)

    @classmethod
    def get_student_attendances(cls, login):

        student_attendances = []

        for attendance in cls.attendances:
            if attendance.student_login == login:
                student_attendances.append(attendance)

        return student_attendances
