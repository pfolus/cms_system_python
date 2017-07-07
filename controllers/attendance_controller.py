def get_average_percent(attendance):
    '''
    Calculates average attendance based on elements in list and it's length
    '''

    attendances_sum = 0

    for number in attendance.student_attendances:
        attendances_sum += number

    attendance.average = attendances_sum / len(attendance.student_attendances)
    attendance.average *= 100



def insert_presence(attendances, login):
    '''
    Appends user's attendance with integer = 1
    '''

    for attendance in attendances:
        if attendance.student_login == login:
            attendance.student_attendances.append(1)
            get_average_percent(attendance)


def insert_absence(attendances, login):
    '''
    Appends user's attendance with integer = 0
    '''

    for attendance in attendances:
        if attendance.student_login == login:
            attendance.student_attendances.append(0)
            get_average_percent(attendance)


def insert_late(attendances, login):
    '''
    Appends user's attendance with integer = 0.8
    '''

    for attendance in attendances:
        if attendance.student_login == login:
            attendance.student_attendances.append(0.8)
            get_average_percent(attendance)
