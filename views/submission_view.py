from views.bcolors import Bcolors


def show_sub(submission):
    login = submission.user_login
    title = submission.title
    answer = submission.answer
    date = submission.date
    score = submission.score
    if submission.is_checked:
        print(Bcolors.GREEN + "\n{}'s submission for assingment: {}:\n <{}>\n sent:{}\n Score:{}".format(
            login, title, answer, date, score) + Bcolors.ENDC)
        print(Bcolors.BLUE + 'It was already checked by the mentor.' + Bcolors.ENDC)
    else:
        print(Bcolors.RED + "\n{}'s submission for assingment: {}:\n <{}>\n sent:{}\n Score:{}".format(
            login, title, answer, date, score) + Bcolors.ENDC)
        print(Bcolors.BLUE + 'It wasn\'t checked by the mentor yet.' + Bcolors.ENDC)
