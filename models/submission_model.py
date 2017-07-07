from datetime import datetime


class Submission:

    def __init__(self, user_login, title, answer, date=datetime.now(), score=0, is_checked=False):
        '''
        Initializes Submission instance

        Args:
            user_login - string
            title - string
            answer - string
            date - datetime object
            score - int
            is_checked - bool
        '''
        self.user_login = user_login
        self.title = title
        self.answer = answer
        self.date = date
        self.score = score
        self.is_checked = is_checked
