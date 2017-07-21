import datetime
from views.bcolors import Bcolors


class Event:

    events = []

    def __init__(self, name, date, login='all', ev_type='Event'):
        self.name = name
        self.date = date.date()
        self.ev_type = ev_type
        self.login = login
        self.is_passed = Event.check_if_passed(self)
        Event.add_to_list(self)

    @classmethod
    def add_to_list(cls, ev_object):
        '''
        Adds every new object, to events list
        '''
        cls.events.append(ev_object)

    @classmethod
    def remove_event(cls, ev_object):
        '''
        Remove chosen event obj from events list

        Parameters
        ----------
        ev_object = Event object

        Returns
        -------
        boolean
        '''
        cls.events.remove(ev_object)

    def check_if_passed(self):
        '''
        Checks whether event is passed, or in the future
        '''
        today = datetime.date.today()

        if self.date < today:
            return True

        else:
            return False
