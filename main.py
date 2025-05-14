from models import StudentApplication, ClassQueue, SchoolSystem
from enums import PrivilegesEnum
from enrollment_algorithms import SimpleEnrollment, ExamEnrollment
from readers_writers import JsonWriter, JsonReader, CsvWriter, CsvReader

def print_queue(queue, title=""):
    print(f"\n{title}")
    for i, app in enumerate(queue.applications, 1):
        print(f"{i}. {app.name} | Діти в сім'ї: {app.family_children} | Пільги: {[p.name for p in app.privileges]} | Дата подачі: {app.date_submitted} | priority_score: {app.priority_score()}")

def demo():
    print("=== Створення школи і класів ===")
    school = SchoolSystem()

    class1 = ClassQueue("1A", 5)
    class2 = ClassQueue("1B", 5)
    school.add_class(class1)
    school.add_class(class2)

    # Створення заявок
    apps = [
        StudentApplication("1st", 2, [PrivilegesEnum.MANY_CHILDREN]),
        StudentApplication("2nd", 1, [PrivilegesEnum.MILITARY]),
        StudentApplication("3th", 2, []),
        StudentApplication("4th", 1, []),
        StudentApplication("5th", 1, [PrivilegesEnum.ORPHAN]),
        StudentApplication("6th", 2, [PrivilegesEnum.ORPHAN]),
        StudentApplication("7th", 3, []),
    ]

    print("\n=== Додавання заявок у черги ===")
    for app in apps:
        shortest_class = school.find_random_queue()
        shortest_class.add_application(app)

    # Показати чергу до сортування
    print_queue(class1, "Черга 1A (до сортування)")
    print_queue(class2, "Черга 1B (до сортування)")

    # Сортування черги
    print("\n=== Сортування черг ===")
    class1.sort_combined()
    class2.sort_by_priority()

    print_queue(class1, "Черга 1A (після комбінованого сортування)")
    print_queue(class2, "Черга 1B (після сортування за пріоритетом)")

    # Видалення заявки
    print("\n=== Видалення заявки ===")
    to_remove = class1.applications[0]
    print(f"Видаляємо заявку: {to_remove.name}")
    class1.remove_application(to_remove)
    print_queue(class1, "Черга 1A (після видалення заявки)")

    # Об'єднання класів
    print("\n=== Об'єднання класів 1A і 1B в 1C ===")
    class3 = school.merge_classes(class1, class2, "1C")
    print_queue(class3, "Черга 1C (після об'єднання)")

    class4 = ClassQueue("1D", 5)
    school.add_class(class4)


    # Читання з файлу
    print("\n=== Зчитування заявок із файлів ===")
    reader_json = JsonReader()
    reader_csv = CsvReader()

    apps_from_csv = reader_csv.read("applications.csv")
    apps_from_json = reader_json.read("applications.json")

    print("\nЗаявки з CSV:")
    for app in apps_from_csv:
        shortest_class = school.find_shortest_queue()
        shortest_class.add_application(app)
        print(f"{app.name} | Пільги: {[p.name for p in app.privileges]}")

    print("\nЗаявки з JSON:")
    for app in apps_from_json:
        shortest_class = school.find_random_queue()
        shortest_class.add_application(app)
        print(f"{app.name} | Пільги: {[p.name for p in app.privileges]}")

    print_queue(class3, "Черга 1С (до сортування)")
    print_queue(class4, "Черга 1D (до сортування)")

    print("\n=== Сортування черг ===")
    class3.sort_combined()
    class4.sort_by_priority()
    print_queue(class3, "Черга 1C (після комбінованого сортування)")
    print_queue(class4, "Черга 1D (після сортування за пріоритетом)")


    # Запис у файл (JSON і CSV)
    print("\n=== Запис черги у файли ===")
    writer_json = JsonWriter()
    writer_csv = CsvWriter()
    writer_json.write("applications_wr.json", class3.applications)
    writer_csv.write("applications_wr.csv", class4.applications)
    print("Файли 'applications.json' та 'applications.csv' створені.")


    # Просте зарахування
    print("\n=== Просте зарахування ===")
    simple_algo = SimpleEnrollment()
    enrolled_students = simple_algo.enroll(class4, class4.max_students)
    for student in enrolled_students:
        print(f"Зараховано (простий алгоритм): {student.name}")

    # Зарахування за іспитом
    print("\n=== Зарахування за іспитом ===")
    exam_algo = ExamEnrollment()
    enrolled_students_exam = exam_algo.enroll(class3, class3.max_students)
    for student in enrolled_students_exam:
        print(f"Зараховано (іспит): {student.name} | Бал: {student.exam_score} | priority_score: {student.priority_score()}")

if __name__ == "__main__":
    demo()
