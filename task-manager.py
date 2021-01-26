"""

"""

from datetime import date
from datetime import datetime


class Task:

    def __init__(self, title, due=None, priority=None, description=""):
        if not type(due) is int:
            raise ValueError('Parameter Due must be unix timestamp')
        now = datetime.now()


        self.title = title
        self.description = description
        self.priority = priority
        self.due = due
        self.created =

class TaskList(list):
    pass


t = Task("test", "21 февраля 2026")
print(t.created)
print(t.due)


