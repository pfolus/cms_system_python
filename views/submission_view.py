def show_sub(submission):
    login = submission.user_login
    title = submission.title
    answer = submission.answer
    date = submission.date
    score = submission.score
    if submission.is_checked:
        print('\033[92m'+"{}'s submission for assingment: {}: <{}> sent:{}, Score:{}".format(
            login, title, answer, date, score)+'\033[0m')
    else:
        print('\033[91m'+"{}'s submission for assingment: {}: <{}> sent:{}, Score:{}".format(
            login, title, answer, date, score)+'\033[0m')
