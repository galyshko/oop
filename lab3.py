from abc import ABC, abstractmethod
from datetime import datetime, timedelta
import time


class Client(ABC):

    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        self.last_deposit = datetime.min
        self.transactions = []  # Історія транзакцій

    @abstractmethod
    def deposit(self, amount):
        pass

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: Зняття {amount} грн")
            print(f"\nЗняття {amount} грн з рахунку {self.name}\nОновлений баланс: {self.balance}")
        else:
            print(f"\nНедостатньо коштів для зняття в {self.name}")

    def transfer(self, amount, to_client):
        if amount <= self.balance:
            self.balance -= amount
            to_client.balance += amount
            self.transactions.append(
                f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: Переказ {amount} грн на рахунок {to_client.name}")
            to_client.transactions.append(
                f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: Отримано {amount} грн від {self.name}")
            print(
                f"\nПереказ {amount} грн від {self.name} на рахунок {to_client.name}\nБаланс відправника: {self.balance}      Баланс отримувача: {to_client.balance}")
        else:
            print(f"\nНедостатньо коштів для переказу в {self.name}")


class PrivatePerson(Client):
    def __init__(self, name, balance=0):
        super().__init__(name, balance)

    def __str__(self):
        return f"{self.name} Тип - Приватний рахунок\nБаланс: {self.balance}"


    def deposit(self, amount):
        if ((datetime.now() - self.last_deposit) < timedelta(seconds=5)):
            print("\nПоповнювати рахунок можна не частіше одного разу на 5 днів.")
        else:
            self.balance += amount
            self.transactions.append(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: Поповнення на {amount} грн")
            self.last_deposit = datetime.now()
            print(f"\nПоповнення рахунку {self.name} на {amount} грн\nОновлений баланс: {self.balance}")




class CorporateClient(Client):
    def __init__(self, name, balance=0):
        super().__init__(name, balance)
        self.salary_count = 0  # Лічильник отриманих зарплат

    def __str__(self):
        return f"{self.name} Тип - Корпоративний рахунок\nБаланс: {self.balance}"

    def deposit(self, amount):
        if self.salary_count < 2 and ((datetime.now() - self.last_deposit) > timedelta(seconds=1)):
            self.balance += amount
            self.transactions.append(
                f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: Поповнення зарплати {amount} грн")
            self.salary_count += 1
            self.last_deposit = datetime.now()
            print(f"\nПоповнення рахунку {self.name} на {amount} грн\nОновлений баланс: {self.balance}")
        else:
            print("\nЗарплату можна отримати не більше двох разів на місяць.")



class Clients:
    def __init__(self):
        self.clients = {}

    def __iter__(self):
        return iter(self.clients.values())

    def __setitem__(self, name, client):
        if name in self.clients:
            print(f"\nПомилка: клієнт {name} вже є у системі.")
        elif isinstance(client, Client):
            self.clients[name] = client
            print(f"\nКлієнта {name} додано до системи.")
        else:
            print("\nПомилка: об'єкт не є клієнтом.")

    def __delitem__(self, name):
        if name in self.clients:
            del self.clients[name]
            print(f"\nКлієнта {name} видалено з системи.")
        else:
            print(f"\nПомилка: клієнта з іменем {name} не знайдено.")

    def show_all_clients(self):
        print("\nСписок клієнтів: ")
        for client in self.clients.values():
            print(f"\n{client.name} \nБаланс: {client.balance} грн")

    def process_transactions(self):
        for client in self.clients.values():
            print(f"\nТранзакції для клієнта {client.name}:")
            if client.transactions:
                for transaction in client.transactions:
                    print(transaction)
            else:
                print("Транзакцій немає.")


def main():
    # Створення клієнтів
    client1 = PrivatePerson("Андрій Вусач")
    client2 = CorporateClient("Семен Геній")
    client3 = PrivatePerson("Маша Контратенко")


    # Створення контейнера для клієнтів
    clients_container = Clients()

    # Додавання клієнтів
    clients_container[client1.name] = client1
    clients_container[client2.name] = client2
    clients_container[client3.name] = client3
    clients_container[client3.name] = client3

    client1.deposit(1000)
    client1.deposit(500)
    time.sleep(5)
    client1.deposit(500)
    client2.deposit(5000)
    client2.deposit(5000)
    time.sleep(1)
    client2.deposit(5000)
    time.sleep(1)
    client2.deposit(5000)

    client1.withdraw(200)
    client2.withdraw(500)
    client3.withdraw(1000)

    clients_container.show_all_clients()
    client2.transfer(1000, client1)
    clients_container.show_all_clients()
    client2.transfer(1000, client3)

    # Виведення балансу та транзакцій для всіх клієнтів
    clients_container.show_all_clients()
    clients_container.process_transactions()

    for elemet in clients_container:
        print(elemet)

    for elemet in clients_container:
        elemet.withdraw(500)


    # Видалення клієнта
    del clients_container["Маша Контратенко"]

    # Повторний вивід списку клієнтів після видалення
    clients_container.show_all_clients()

if __name__ == "__main__":
    main()
