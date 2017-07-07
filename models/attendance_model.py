class Attendance:

    def __init__(self, student_login, student_attendances=[], average=float(0)):
        '''
        Initializes Attendance object

        Args:
            student_login - string
            student_attendances - list with ints
            average - float
        '''
        self.student_login = student_login
        self.student_attendances = student_attendances
        self.average = average
