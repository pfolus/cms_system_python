class Shoutbox:

    messages = []

    def __init__(self,date, author, message):
        self.date = date
        self.author = author
        self.message = message

        Shoutbox.add_message(self)

    @classmethod
    def add_message(cls, object):
        cls.messages.append(object)

    @classmethod
    def get_recent_messages(cls):
        max_messages = 30
        if len(cls.messages) >= max_messages:
            return cls.messages[-max_messages:]
        else:
            return cls.messages
