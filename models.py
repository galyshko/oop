import gc
from datetime import datetime
from zope.interface import implementer
from interfaces import IQueueManager
from enums import PrivilegesEnum
import random

class StudentApplication:
    def __init__(self, name: str, family_children: int, privileges: list[PrivilegesEnum]):
        self.name = name
        self.family_children = family_children
        self.privileges = privileges
        self.date_submitted = datetime.now()
        self.exam_score = None  # буде встановлюватись при іспиті

    def priority_score(self):
        return sum(p.value for p in self.privileges) + self.family_children

@implementer(IQueueManager)
class ClassQueue:
    def __init__(self, class_name: str, max_students: int):
        self.class_name = class_name
        self.max_students = max_students
        self.applications = []

    def add_application(self, application: StudentApplication):
        self.applications.append(application)

    def remove_application(self, application: StudentApplication):
        self.applications.remove(application)

    def merge_queue(self, other_queue):
        self.applications.extend(other_queue.applications)

    def sort_by_submission(self):
        self.applications.sort(key=lambda app: app.date_submitted)

    def sort_by_priority(self):
        self.applications.sort(key=lambda app: app.priority_score(), reverse=True)

    def sort_combined(self):
        def sort_key(app):
            priority = app.priority_score()
            is_privileged = priority >= 10  # тільки якщо бал 10 або більше - це пільговик

            if is_privileged:
                # Пільговики: спочатку за балом (спаданням), потім по даті
                return (0, -priority, app.date_submitted)
            else:
                # Без пільг: ідуть після, тільки дата
                return (1, app.date_submitted)

        self.applications.sort(key=sort_key)

        self.applications.sort(key=sort_key)

class SchoolSystem:
    def __init__(self):
        self.classes = []

    def add_class(self, class_queue: ClassQueue):
        self.classes.append(class_queue)

    def find_shortest_queue(self):
        return min(self.classes, key=lambda c: len(c.applications))

    def find_random_queue(self):
        return random.choice(self.classes)

    def merge_classes(self, class1, class2, new_class_name):
        new_class = ClassQueue(new_class_name, class1.max_students + class2.max_students)
        new_class.applications = class1.applications + class2.applications
        self.add_class(new_class)
        self.classes.remove(class1)
        self.classes.remove(class2)

        return new_class

