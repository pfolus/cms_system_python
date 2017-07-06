from views.bcolors import Bcolors


def show_assingment(assingment, number):
    title = assingment.title
    content = assingment.content
    date = assingment.date
    max_grade = assingment.max_grade

    print(Bcolors.BOLD + '{}. {}:\n{}\nDeadline: {}\nScoring: 0-{}\n'.format(
        number, title, content, date, max_grade) + Bcolors.ENDC)
