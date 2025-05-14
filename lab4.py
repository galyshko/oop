import platform

class OSConditionalMeta(type):
    def __new__(cls, name, bases, attrs):
        current_os = platform.system()
        print(f"Створення класу {name} для ОС: {current_os}")

        # Залежно від ОС, видаляємо або залишаємо методи
        if current_os == "Windows":
            # Видалити метод only_for_linux, якщо є
            if "only_for_linux" in attrs:
                print("Видалення only_for_linux для Windows")
                del attrs["only_for_linux"]
        elif current_os == "Linux":
            # Видалити метод only_for_windows, якщо є
            if "only_for_windows" in attrs:
                print("Видалення only_for_windows для Linux")
                del attrs["only_for_windows"]

        return super().__new__(cls, name, bases, attrs)

# Клас, який використовує метаклас
class MyTool(metaclass=OSConditionalMeta):
    def only_for_windows(self):
        return "Це працює тільки на Windows"

    def only_for_linux(self):
        return "Це працює тільки на Linux"

    def always_available(self):
        return "Це завжди доступно"

# Тестування
tool = MyTool()
print(tool.always_available())

# Виклик методів залежно від доступності
if hasattr(tool, "only_for_windows"):
    print(tool.only_for_windows())
else:
    print("Метод only_for_windows недоступний")

if hasattr(tool, "only_for_linux"):
    print(tool.only_for_linux())
else:
    print("Метод only_for_linux недоступний")
print(tool.__dir__())
