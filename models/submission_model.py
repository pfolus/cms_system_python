from datetime import datetime


class Submission:

    def __init__(self, user_login, title, answer):
        self.user_login = user_login
        self.title = title
        self.answer = answer
        self.date = datetime.now()
        self.score = 0
        self.is_checked = False
