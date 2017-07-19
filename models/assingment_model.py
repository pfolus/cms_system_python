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
