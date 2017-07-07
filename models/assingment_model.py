class Assingment:

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
