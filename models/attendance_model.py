from datetime import datetime


class Attendance:

    attendances = []

    def __init__(self, student_login, value, date=datetime.today().date()):
        '''
        Initializes Attendance object
        Args:
            student_login - string
            student_attendances - list with ints
            average - float
        '''
        self.student_login = student_login
        self.value = value
        self.date = date
        Attendance.add_to_list(self)

    @classmethod
    def add_to_list(cls, att_object):

        cls.attendances.append(att_object)

    @classmethod
    def get_student_attendances(cls, login):
        '''
        Returns list of attendances which have student_login as atribute

        Args:
            login - string

        Returns:
            list - with Attendance object
        '''

        student_attendances = []

        for attendance in cls.attendances:
            if attendance.student_login == login:
                student_attendances.append(attendance)

        return student_attendances

    @classmethod
    def get_student_attendance_by_date(cls, login, date):
        '''
        Returns attendance with given login and date

        Args:
            login - string
            date - datetime object

        Returns:
            attendance - Attendance object
        '''

        for attendance in cls.attendances:

            if attendance.student_login == login and attendance.date == date:

                return attendance
