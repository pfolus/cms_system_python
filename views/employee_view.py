from controllers.student_controller import calculate_grades


def show_students_list(students_list):
    '''
    Show students name and surname from student's list

    Args:
        students_list - list with Student objects
    '''
    index = 1
    print()
    for student in students_list:
        print('({}) {} {}'.format(index, student.name, student.surname))
        index += 1
    print()


def show_students_list_detailed(canvas):
    '''
    Show detailes student's list

    Args:
        canvas - objact with lists containing objects of other classess
    '''
    index = 1
    student_attendance = 0
    print()
    for student in canvas.students:
        [grades_sum,
         max_grades_sum,
         amount_of_grades] = calculate_grades(canvas.assingments,
                                              canvas.submissions,
                                              student.login)

        for attendance in canvas.attendances:
            if attendance.student_login == student.login:
                student_attendance = attendance.average

        print('({}) {} {}, Score: {}/{}, Attendance: {:.4}%'.format(index, student.name, student.surname, grades_sum, max_grades_sum, student_attendance))

        index += 1
    print()
