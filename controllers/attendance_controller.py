def get_average_percent(attendance):

    attendances_sum = 0

    for number in attendance.student_attendances:
        attendances_sum += number

    attendance.average = attendances_sum / len(attendance.student_attendances)
    att.average *= 100



def insert_presence(attendances, login):

    for attendance in attendances:
        if attendance.student_login == login:
            attendance.student_attendances.append(1)
            get_average_percent(attendance)


def insert_absence(attendances, login):

    for attendance in attendances:
        if attendance.student_login == login:
            attendance.student_attendances.append(0)
            get_average_percent(attendance)


def insert_late(attendances, login):

    for attendance in attendances:
        if attendance.student_login == login:
            attendance.student_attendances.append(0.8)
            get_average_percent(attendance)
