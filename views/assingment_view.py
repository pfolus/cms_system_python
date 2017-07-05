def show_assingment(assingment):
    title = assingment.title
    content = assingment.content
    date = assingment.date
    max_grade = assingment.max_grade

    print('{}:\n {}\nDeadline: {}\nScoring: 0-{}'.format(
        title, content, date, max_grade))
