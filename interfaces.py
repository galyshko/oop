from zope.interface import Interface

class IDataReader(Interface):
    def read(file_path: str):
        """Зчитування даних із файлу"""

class IDataWriter(Interface):
    def write(file_path: str, data):
        """Запис даних у файл"""

class IQueueManager(Interface):
    def add_application(application):
        """Додати заявку до черги"""

    def remove_application(application):
        """Видалити заявку з черги"""

    def merge_queue(other_queue):
        """Об'єднати черги"""

class IEnrollmentAlgorithm(Interface):
    def enroll(queue, max_students: int):
        """Алгоритм зарахування дітей"""
