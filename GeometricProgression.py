class GeometricProgression:
    instances = []  # Статична змінна для збереження екземплярів класу

    def __init__(self, a, b):
       #Ініціалізація геометричної прогресії з першим елементом a і знаменником b
        if b == 0:
            raise ValueError("Знаменник прогресії не може бути нульовим.")
        self.a = a
        self.b = b
        GeometricProgression.instances.append(self)

    def nth_element(self, n):
        #Обчислює n-й елемент геометричної прогресії
        return self.a * (self.b ** (n - 1))

    def sequence(self, k, m):
        #Генерує список елементів прогресії від k-го до m-го включно
        return [self.nth_element(i) for i in range(k, m + 1)]

    def update_params(self, a, b):
        #Оновлює параметри прогресії (перший елемент і знаменник)
        if b == 0:
            raise ValueError("Знаменник прогресії не може бути нульовим.")
        self.a = a
        self.b = b

    def __eq__(self, other):
        #Перевіряє рівність двох прогресій за першими елементами і знаменником
        if isinstance(other, GeometricProgression):
            return self.a == other.a and self.b == other.b
        return False

    def __str__(self):
        #Повертає рядкове представлення перших семи елементів прогресії
        first_seven = self.sequence(1, 7)
        return f"& {self.a}, {self.b}: {first_seven}"

    @staticmethod
    def show_instances():
       #Виводить інформацію про всі існуючі екземпляри прогресій
        for instance in GeometricProgression.instances:
            print(instance)


# Створення екземплярів
gp1 = GeometricProgression(1, 2)
gp2 = GeometricProgression(2, 2)
gp3 = GeometricProgression(2, 0.5)

# Виведення інформації
print(gp1)
print(gp2)
print(gp3)

# Отримання 5-го елемента
print("\n5-й елемент gp1:", gp1.nth_element(5))

# Послідовність від 3-го до 6-го елемента
print("\nЕлементи з 3 по 6 gp2:", gp2.sequence(3, 6))

# Зміна параметрів
gp1.update_params(2, 0.5)
print("\ngp1 Після зміни параметрів:", gp1)

# Перевірка рівності
print("\nЧи рівні gp1 і gp3?", gp1 == gp3)

# Виведення всіх екземплярів
GeometricProgression.show_instances()
