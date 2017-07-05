def show_students_list(students_list):
    index = 1
    for student in students_list:
        print('{}. {} {}'.format(index, student.name, student.surname))
        index += 1


def show_students_list_detailed(canvas):
    # TODO
    pass
