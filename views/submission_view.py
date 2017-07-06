from views.bcolors import Bcolors


def show_sub(submission):
    login = submission.user_login
    title = submission.title
    answer = submission.answer
    date = submission.date
    score = submission.score
    if submission.is_checked:
        print(Bcolors.GREEN + "\n{}'s submission for assingment: {}\n<{}>\nSent: {}\nScore: {}".format(
            login, title, answer, date, score) + Bcolors.ENDC)
        print(Bcolors.BLUE + '\nIt was already checked by the mentor.\n' + Bcolors.ENDC)
    else:
        print(Bcolors.RED + "\n{}'s submission for assingment: {}\n<{}>\nSent: {}\nScore: {}".format(
            login, title, answer, date, score) + Bcolors.ENDC)
        print(Bcolors.BLUE + Bcolors.BOLD + '\nIt wasn\'t checked by the mentor yet.\n' + Bcolors.ENDC)
