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
        cls.events.append(ev_object)

    @classmethod
    def remove_event(cls, ev_object):
        cls.events.remove(ev_object)

    def check_if_passed(self):
        today = datetime.date.today()

        if self.date < today:
            return True

        else:
            return False

    def __str__(self):
        if self.is_passed:
            return(Bcolors.RED + '{} | {} | {}'.format(self.name, self.date, self.ev_type) + Bcolors.ENDC)
        else:
            return(Bcolors.BOLD + '{} | {} | {}'.format(self.name, self.date, self.ev_type) + Bcolors.ENDC)
