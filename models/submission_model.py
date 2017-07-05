from datetime import datetime


class Submission:

    def __init__(self, user_login, title, answer, date=datetime.now(), score=0, is_checked=False):
        self.user_login = user_login
        self.title = title
        self.answer = answer
        self.date = date
        self.score = score
        self.is_checked = is_checked
