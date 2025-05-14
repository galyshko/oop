import random
from zope.interface import implementer
from interfaces import IEnrollmentAlgorithm

@implementer(IEnrollmentAlgorithm)
class SimpleEnrollment:
    def enroll(self, queue, max_students: int):
        return queue.applications[:max_students]

@implementer(IEnrollmentAlgorithm)
class ExamEnrollment:
    def enroll(self, queue, max_students: int):
        # Генеруємо бали
        for app in queue.applications:
            app.exam_score = random.randint(0, 100)

        max_score = max(app.exam_score for app in queue.applications)
        passing_score = 0.6 * max_score

        # Пільговики (priority_score >= 10) і склали іспит
        privileged_apps = [
            app for app in queue.applications
            if app.priority_score() >= 10 and app.exam_score >= passing_score
        ]

        # Непільговики (priority_score < 10) і склали іспит
        non_privileged_apps = [
            app for app in queue.applications
            if app.priority_score() < 10 and app.exam_score >= passing_score
        ]

        # Сортуємо по балах
        privileged_apps.sort(key=lambda app: app.exam_score, reverse=True)
        non_privileged_apps.sort(key=lambda app: app.exam_score, reverse=True)

        # Формуємо фінальний список
        selected = privileged_apps[:max_students]
        if len(selected) < max_students:
            selected += non_privileged_apps[:max_students - len(selected)]

        return selected