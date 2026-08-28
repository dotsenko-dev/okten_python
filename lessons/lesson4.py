####################################################################################
# GENERATORS, ITERATORS, FILES & STRUCTURAL PATTERN MATCHING
# (Ітератори, генератори, робота з файлами, серіалізація та Structural Pattern Matching)
####################################################################################

################################## 1. ІТЕРАТОРИ ТА ГЕНЕРАТОРИ (GENERATORS & ITERATORS)
# Генератор — це функція, яка повертає ітератор і випускає значення по одному за допомогою `yield`.
# Генератор вираз (generator expression) створюється через круглі дужки `()`,
# не завантажує весь список у пам'ять (на відміну від List Comprehension `[]`).

# 1.1. Generator Expression проти List Comprehension
# l = [i for i in range(50_000_000)] # Створить список у пам'яті (~400+ MB)
g_exp = (i for i in range(50_000_000))  # Створить генератор (займає лічені байти)

# 1.2. Отримання елементів через next() та обробка StopIteration
# Якщо викликів next() більше, ніж елементів — Python згенерує помилку StopIteration.
g = (i for i in range(2))
# print(next(g))  # 0
# print(next(g))  # 1
# print(next(g))  # Викине StopIteration! Потрібно обгортати в try-except або цикл for

# 1.3. Перехоплення StopIteration та значення з return
from collections.abc import Iterator


def gen_with_return() -> Iterator[int | str]:
    yield 1
    yield 2
    # значення return повертається як аргумент винятку StopIteration(e.value)
    return "my return"


g_ret = gen_with_return()
try:
    print(next(g_ret))  # 1
    print(next(g_ret))  # 2
    print(next(g_ret))  # Викине StopIteration
except StopIteration as e:
    print(f"Генератор завершено. Повернуте значення: {e.value}")  # 'my return'


# 1.4. Нескінченний генератор (Lazy evaluation)
import uuid


def gen_jpg_file() -> Iterator[str]:
    pattern = "{}.jpg"
    while True:
        # Генерує унікальне ім'я файлу на кожній ітерації за вимогою
        yield pattern.format(uuid.uuid1())


file_gen = gen_jpg_file()
# print(next(file_gen)) # e.g. 550e8400-e29b-41d4-a716-446655440000.jpg


# 1.5. Кругова черга / Круговий розклад (Round-Robin) через генератори
def gen1(n: int):
    for i in range(1, n + 1):
        yield f"{i} - Team1"


def gen2(n: int):
    for i in range(1, n + 1):
        yield f"{i} - Team2"


# Чередування виконання двох генераторів по черзі:
teams = [gen1(3), gen2(2)]
while teams:
    team = teams.pop(0)
    try:
        print(next(team))
        teams.append(team)  # Повертаємо в кінець черги, якщо є елементи
    except StopIteration:
        pass  # Якщо елементи закінчилися — генератор більше не повертається в чергу


################################## 2. СТВОРЕННЯ ВЛАСНИХ ІТЕРАБЕЛЬНИХ ОБ'ЄКТІВ (ITERABLE CLASSES)
# Щоб зробити власний клас ітерабельним, потрібно реалізувати magic-методи:
# __iter__(self) -> повертає сам об'єкт-ітератор
# __next__(self) -> повертає наступне значення або генерує StopIteration


# 2.1. Класовий підхід (реалізація протоколу Iterator)
class MyRange:
    def __init__(self, length: int) -> None:
        self.__length = length
        self.__counter = 0

    def __iter__(self):
        return self

    def __next__(self) -> int:
        if self.__counter < self.__length:
            res = self.__counter
            self.__counter += 1
            return res
        raise StopIteration  # Сигнал для циклу for про закінчення даних


# for i in MyRange(3):
#     print(i)


# 2.2. Функціональний підхід (аналог через генератор)
def my_range(length: int):
    count = 0
    while count < length:
        yield count
        count += 1


################################## Коротка шпаргалка ітераторів
# yield                  → тимчасово зупиняє функцію та повертає значення (зберігає стан)
# next(g)                → запитує наступне значення у генератора
# StopIteration          → виняток, що повідомляє про вичерпання ітератора
# __iter__() / __next__() → методи для створення власних ітерабельних класів


####################################################################################
# WORK WITH FILES (Робота з файлами, режими доступу та контекстні менеджери)
####################################################################################

# Основні режими відкриття файлів:
# "r"  → читання (помилка, якщо файлу немає)
# "w"  → перезапис (створює новий або ОЧИЩАЄ існуючий)
# "a"  → дозапис у кінець (append)
# "x"  → ексклюзивне створення (помилка, якщо файл ВЖЕ існує)
# "b"  → бінарний режим (rb, wb — для зображень, аудіо тощо)
# "+"  → розширений режим (r+ — читання+запис, w+ — запис+читання з очищенням)

# 1. Контекстний менеджер `with` автоматично закриває файл навіть при помилках:
try:
    with open("1.txt", mode="w", encoding="utf-8") as file:
        file.write("Hello from write\nHi")
except Exception as e:
    print(f"Помилка створення файлу: {e}")

try:
    with open("1.txt", mode="r+", encoding="utf-8") as file:
        file.write("Hello")
        file.seek(0)  # Переміщує вказівник читання/запису на початок файлу
        content = file.read()
except Exception as e:
    print(f"Помилка читання файлу: {e}")

# 2. Множинні контекстні менеджери (копіювання бінарного файлу з генерацією імені)
# Синтаксис з дужками with (...) доступний у Python 3.10+
# try:
#     with (
#         open("lessons/download.jpg", mode="rb") as file_in,
#         open(next(gen_jpg_file()), mode="wb") as file_out,
#     ):
#         file_out.write(file_in.read())
# except Exception as e:
#     print(f"Помилка при копіюванні: {e}")


################################## Коротка шпаргалка файлових операцій
# with open(...) as f    → безпечна робота з файлами (гарантоване закриття)
# file.seek(0)           → переміщення курсора у файлі
# file.read() / readline → читання всього файлу / одного рядка
# mode="rb" / "wb"       → робота з бінарними файлами (зображення, архіви)


####################################################################################
# SERIALIZATION: JSON & PICKLE (Серіалізація та збереження даних)
####################################################################################

# JSON — текстовий формат, універсальний для багатьох мов прогрумування.
# Pickle — бінарний формат, специфічний ТІЛЬКИ для Python (підтримує складні об'єкти).

import json
import pickle
from typing import TypedDict

UserDict = TypedDict("UserDict", {"name": str, "age": int})

users_data: list[UserDict] = [
    {"name": "Max", "age": 14},
    {"name": "Karina", "age": 44},
    {"name": "Makar", "age": 49},
]

# 1. Робота з JSON (text mode)
try:
    with open("users.json", mode="w", encoding="utf-8") as file:
        json.dump(users_data, file, indent=4)  # Серіалізація у файл

    with open("users.json", mode="r", encoding="utf-8") as file:
        loaded_json: list[UserDict] = json.load(file)  # Десеріалізація
except Exception as e:
    print(f"JSON Error: {e}")

# 2. Робота з Pickle (binary mode)
try:
    with open("users.data", mode="wb") as file:
        pickle.dump(users_data, file)  # Запис бінарних даних

    with open("users.data", mode="rb") as file:
        loaded_pickle: list[UserDict] = pickle.load(file)  # Читання
        print("Завантажені дані з Pickle:", loaded_pickle)
except Exception as e:
    print(f"Pickle Error: {e}")


################################## Коротка шпаргалка серіалізації
# json.dump(obj, file)   → зберегти об'єкт у JSON файл
# json.load(file)        → зчитати об'єкт з JSON файлу
# pickle.dump(obj, file) → зберегти Python-об'єкт у бінарний файл (.data/.pkl)
# pickle.load(file)      → відновити Python-об'єкт з бінарного файлу


####################################################################################
# STRUCTURAL PATTERN MATCHING (Конструкція match / case)
####################################################################################
# З'явилася в Python 3.10. Дозволяє зіставляти структури даних, послідовності та об'єкти класів.


# 1. Просте зіставлення та зіставлення кортежів/списків
cmd = ["left", "300"]

match cmd:
    case "hi":
        print("hello")
    case ["left", value]:
        print(f"Рух ліворуч на {value}")
    case ["left" as direction, "200" as val]:
        print(direction, val)
    case f, s, t:
        print(f"Три елементи: {f}, {s}, {t}")
    case _:  # Wildcard (аналог else/default)
        print("Команду не розпізнано")


# 2. Pattern Matching з об'єктами та словниками
# __match_args__ вказує порядок позиційних аргументів для case User(...)
class UserEntity:
    __match_args__ = ("name", "age")

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


def matcher(source: UserEntity | dict):
    match source:
        # Зіставлення зі структурою класу через __match_args__
        case UserEntity(name, age):
            print(f"[Class Match] User: {name}, Age: {age}")

        # Зіставлення зі словником та точна перевірка значення поля ("Karina")
        case {"name": "Karina" as name, "age": age}:
            print(f"[Dict Match] Found Karina with age {age}")

        case {"name": name, "age": age}:
            print(f"[Dict Match] Custom user: {name}, {age}")


user_obj = UserEntity("Karina", 43)
matcher(user_obj)


################################## Коротка шпаргалка Pattern Matching
# match val / case ...   → аналог switch/case, але значно потужніший
# case _:                → дефолтна гілка, якщо жоден варіант не підійшов
# __match_args__         → кортеж атрибутів класу для підтримки позиційного match