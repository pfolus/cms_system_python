from operator import attrgetter
from datetime import datetime


class Assingment:

    assingments = []

    def __init__(self, title, content, date, max_grade):
        '''
        Initializes Assignment instance

        Args:
            title - string
            content - string
            date - datetime object
            max_grade - int
        '''
        self.title = title
        self.content = content
        self.date = date
        self.max_grade = max_grade
        Assingment.add_to_list(self)

    @classmethod
    def add_to_list(cls, object):
        cls.assingments.append(object)

    @classmethod
    def get_assingment_by_index(cls, index):
        return cls.assingments[index]

    @classmethod
    def get_coming_assingments(cls):
        sorted_assingments = []

        for assingment in cls.assingments:
            if assingment.date > datetime.today():
                sorted_assingments.append(assingment)

        sorted_assingments.sort(key=attrgetter('date'))

        if len(sorted_assingments) > 2:
            return sorted_assingments[0:3]
        else:
            return sorted_assingments
