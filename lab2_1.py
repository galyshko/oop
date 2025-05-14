from abc import ABC, abstractmethod

# Базовий клас для схем нарахування зарплати
class SalaryScheme(ABC):
    @abstractmethod
    def calculate_salary(self, **kwargs):
        pass

# Фіксована зарплата
class FixedSalary(SalaryScheme):
    def calculate_salary(self, base_salary):
        return base_salary

# Погодинна зарплата
class HourlySalary(SalaryScheme):
    def calculate_salary(self, hourly_rate, hours_worked):
        return hourly_rate * hours_worked

# Комбінована зарплата
class MixedSalary(SalaryScheme):
    def calculate_salary(self, base_salary, hourly_rate, hours_worked, bonus):
        return base_salary + (hourly_rate * hours_worked) + bonus

# Клас для представлення посади
class Position:
    def __init__(self, title, salary_scheme):
        self.title = title  # Назва посади
        self.salary_scheme = salary_scheme  # Тип схеми нарахування зарплати
        self.employees = []  # Список працівників на цій посаді

    def add_employee(self, employee):
        if employee not in self.employees:
            self.employees.append(employee)  # Додаємо працівника

    def remove_employee(self, employee):
        if employee in self.employees:
            self.employees.remove(employee)  # Видаляємо працівника

    def __str__(self):
        employee_names = ", ".join(emp.name for emp in self.employees) if self.employees else "\nНемає працівників"
        return f"\nПосада: {self.title}, Працівники: {employee_names}"

# Клас для представлення працівника
class Employee:
    def __init__(self, name):
        self.name = name  # Ім'я працівника
        self.position = None  # Початково без посади
        self.salary_details = {}  # Параметри для розрахунку зарплати

    def set_position(self, position):
        # Якщо вже є посада, видаляємо працівника з неї
        if self.position:
            self.position.remove_employee(self)
        self.position = position
        position.add_employee(self)  # Додаємо до нової посади

    def set_salary_details(self, **kwargs):
        # Встановлюємо деталі зарплати
        self.salary_details = kwargs

    def calculate_salary(self):
        # Обчислюємо зарплату, якщо є посада
        if self.position:
            salary_scheme = self.position.salary_scheme
            return salary_scheme.calculate_salary(**self.salary_details)
        return 0

    def __str__(self):
        position_info = self.position.title if self.position else "Без посади"
        return f"\n{self.name} ({position_info}): {self.calculate_salary()} грн"

# Клас для представлення компанії
class Company:
    def __init__(self, name):
        self.name = name  # Назва компанії
        self.employees = []  # Список працівників

    def add_employee(self, employee):
        # Додаємо працівника до компанії, якщо його ще немає
        if employee not in self.employees:
            self.employees.append(employee)
            print(f"\nВ {self.name} додано працівника {employee.name}")
        else:
            print(f"\nПомилка! Співробітника {employee.name} вже в {self.name}")

    def remove_employee(self, employee):
        # Видаляємо працівника з компанії та скидаємо його посаду
        if employee in self.employees:
            self.employees.remove(employee)
            if employee.position:
                employee.position.remove_employee(employee)  # Видаляємо з посади
                employee.position = None
            print(f"\nПрацівника {employee.name} звільнено з {self.name}")
        else:
            print(f"\nПомилка! В {self.name} немає співробітника {employee.name}")

    def total_salary_expenses(self):
        # Обчислюємо загальні витрати на зарплату
        return sum(emp.calculate_salary() for emp in self.employees)

    def __str__(self):
        print(f"\nСпівробітники {self.name}:")
        return "".join(str(emp) for emp in self.employees) if self.employees else "Немає працівників"

# Створення посад з різними схемами нарахування зарплат
engineer_position = Position("Інженер", FixedSalary())
worker_position = Position("Робітник", HourlySalary())
manager_position = Position("Менеджер", MixedSalary())

# Створення працівників
employee1 = Employee("Андрій Вусач")
employee2 = Employee("Семен Геній")
employee3 = Employee("Петро Щур")
employee4 = Employee("Маша Контратенко")

# Створення компанії та додавання працівників
company = Company("Cisco")
company.add_employee(employee1)
company.add_employee(employee1)  # Повторне додавання викличе помилку
company.add_employee(employee2)
company.add_employee(employee3)
company.add_employee(employee4)

# Призначення посад працівникам
employee1.set_position(engineer_position)
employee2.set_position(worker_position)
employee3.set_position(manager_position)
employee4.set_position(worker_position)

# Встановлення деталей зарплати
employee1.set_salary_details(base_salary=50000)
employee2.set_salary_details(hourly_rate=200, hours_worked=160)
employee3.set_salary_details(base_salary=30000, hourly_rate=150, hours_worked=120, bonus=15000)
employee4.set_salary_details(hourly_rate=200, hours_worked=100)

# Виведення інформації про компанію та загальні витрати на зарплату
print(company)
print(f"\nЗагальні витрати на зарплати: {company.total_salary_expenses()} грн")

# Зміна посади та зарплати для працівника
employee4.set_position(engineer_position)
employee4.set_salary_details(base_salary=50000)
print(company)
print(f"\nЗагальні витрати на зарплати: {company.total_salary_expenses()} грн")

# Звільнення працівника
company.remove_employee(employee4)
print(company)

# Додаткові перевірки
company.remove_employee(employee4)  # Повторне видалення викличе помилку
print(engineer_position)
print(employee4)

# Підрахунок витрат на зарплату після змін
print(f"\nЗагальні витрати {company.name} на зарплати: {company.total_salary_expenses()} грн")
