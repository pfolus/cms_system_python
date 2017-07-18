from controllers.student_controller import calculate_grades


def show_students_list(students):
    '''
    Prints every student info in new line

    Paramaters
    ----------
    students_list = list (of Student obj)

    Returns
    -------
    None
    '''
    index = 1
    print()
    for student in students:
        print('({}) {} {}'.format(index, student.name, student.surname))
        index += 1
    print()


def show_students_list_detailed(students, attendances, assingments, submissions):
    '''
    Prints detailed info about every student in new line

    Paramaters
    ----------
    canvas = obj of Canvas class

    Returns
    -------
    None
    '''
    index = 1
    student_attendance = 0
    print()
    for student in students:
        [grades_sum,
         max_grades_sum,
         amount_of_grades] = calculate_grades(assingments,
                                              submissions,
                                              student.login)

        for attendance in attendances:
            if attendance.student_login == student.login:
                student_attendance = attendance.average

        print('({}) {} {}, Score: {}/{}, Attendance: {:.4}%'.format(index, student.name, student.surname, grades_sum, max_grades_sum, student_attendance))

        index += 1
    print()
