def show_assingment(assingment, number):
    title = assingment.title
    content = assingment.content
    date = assingment.date
    max_grade = assingment.max_grade

    print('\n{}. {}:\n {}\nDeadline: {}\nScoring: 0-{}'.format(
        number, title, content, date, max_grade))
