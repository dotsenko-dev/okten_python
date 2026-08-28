####################################################################################
# OBJECT-ORIENTED PROGRAMMING / ООП (Основи класів, інкапсуляція, наслідування)
####################################################################################

################################## ОСНОВИ КЛАСУ, SLOTS ТА СТАЙЛГУИД
# Назви класів завжди пишуться в CamelCase.
# __slots__ обмежує набір атрибутів, які можна створювати в екземплярі (заощаджує пам'ять)
class User:
    __slots__ = ("age", "name")  # Дозволено створювати ТІЛЬКИ name та age
    count = 0  # Атрибут класу (спільний для всіх екземплярів)

    def __init__(self, name: str, age: int):
        self.name = name  # Атрибут екземпляра
        self.age = age

    def get_name(self) -> str:
        return self.name

    def __str__(self) -> str:  # Викликається при print(user) або str(user)
        return f"{self.name} {self.age}"

    def __repr__(self) -> str:  # Викликається при відображенні списку [user1, user2]
        return self.__str__()


# user = User("Max", 44)
# user.age = 88                 # Пряма зміна атрибута (без інкапсуляції)
# user.house = 44               # Викине помилку (AttributeError), бо "house" немає в __slots__


################################## ІНКАПСУЛЯЦІЯ ТА РІВНІ ДОСТУПУ (PUBLIC, PROTECTED, PRIVATE)
# Інформаційне приховування:
# self.name     → Public (публічний доступ)
# self._age     → Protected (умовний захист: для внутрішнього використання та класів-нащадків)
# self.__name   → Private (суворий захист: Python змінює ім'я на _User__name — Name Mangling)


class UserEncapsulated:
    count = 0  # Публічна змінна класу
    __private_count = 0  # Приватна змінна класу

    def __init__(self, name: str, age: int):
        self.__name = name  # Приватне поле (Private)
        self._age = age  # Захищене поле (Protected)

    def get_name(self):
        return self.__name


# user = UserEncapsulated("Max", 33)
# print(user.get_name())         # Правильний спосіб доступу через метод
# print(user._age)              # Працює, але це порушення домовленості Protected
# print(user._UserEncapsulated__name) # Працює (Name Mangling), але приватність у Python чисто умовна


################################## НАСЛІДУВАННЯ (INHERITANCE) ТА SUPER()
# Наслідування дозволяє розширювати функціонал інших класів.
# Python підтримує множинне наслідування (перераховуються через кому в дужках).


class Tools:
    def greeting(self):
        print("Hello")

    def go_to_home(self):
        print("Welcome to home")


class Car:
    def start(self):
        print("Welcome to car")


# Клас Parent успадковує всі методи від UserEncapsulated, Tools та Car:
class Parent(UserEncapsulated, Tools, Car):
    def __init__(self, name: str, age: int, status: bool):
        # super().__init__() викликає конструктор батьківського класу (UserEncapsulated)
        super().__init__(name, age)
        self.status = status

    def get_status(self) -> bool:
        return self.status


# parent = Parent("Oleg", 89, True)
# parent.go_to_home()            # З упадковано від Tools
# parent.greeting()              # Успадковано від Tools
# parent.start()                 # Успадковано від Car
# print(parent.get_status())     # Власний метод класу Parent


################################## ГЕТЕРИ, СЕТЕРИ ТА PROPERTIES (@property)
# Контрольований доступ до приватних полів за допомогою геттерів/сеттерів або декоратора @property.


class UserProperty:
    def __init__(self, name: str) -> None:
        self.__name = name

    # 1. Застарілий підхід (ручна реалізація з перевіркою пароля)
    def get_name_with_pass(self, password: str):
        if password == "1111":
            return self.__name
        return "Error"

    # 2. Сучасний підхід Pythonic — Декоратори @property
    @property
    def name(self) -> str:  # Геттер: викликається при читанні user.name
        return self.__name

    @name.setter
    def name(self, name: str):  # Сеттер: викликається при user.name = "Нове ім'я"
        self.__name = name

    @name.deleter
    def name(self):  # Делетер: викликається при del user.name
        del self.__name


# user = UserProperty("Max")
# print(user.name)              # Max (викликає @property)
# user.name = "Albina"          # Зміна значення (викликає @name.setter)
# del user.name                 # Видалення поля (викликає @name.deleter)


################################## Коротка шпаргалка ООП та інкапсуляції
# __slots__ = (...)             → обмежує динамічне створення атрибутів
# self.x / self._x / self.__x   → Public / Protected / Private змінні
# super().__init__()            → виклик конструктора базового (батьківського) класу
# @property / @name.setter      → створює кероване поле (геттер і сеттер) з верифікацією


####################################################################################
# POLYMORPHISM & ABSTRACT CLASSES (поліморфізм та абстрактні класи)
####################################################################################

from abc import ABC, abstractmethod

# Поліморфізм дозволяє об'єктам різних класів мати однаковий інтерфейс (методи).
# ABC (Abstract Base Class) забороняє створювати екземпляр самого класу Shape.
# @abstractmethod зобов'язує всі дочірні класи обов'язково реалізувати ці методи.


class Shape(ABC):
    @abstractmethod
    def area(self) -> int:
        return 0

    @abstractmethod
    def perimeter(self) -> int:
        return 0


class Triangle(Shape):
    def __init__(self, a: int, b: int, c: int) -> None:
        self.a, self.b, self.c = a, b, c

    def area(self) -> int:
        return self.a * self.b * self.c

    def perimeter(self) -> int:
        return self.a + self.b + self.c


class Rectangle(Shape):
    def __init__(self, a: int, b: int) -> None:
        self.a, self.b = a, b

    def area(self) -> int:
        return self.a * self.b

    def perimeter(self) -> int:
        return (self.a + self.b) * 2


# shapes: list[Shape] = [Triangle(4, 2, 3), Rectangle(3, 7)]
# for shape in shapes:
#     print(shape.area())        # Викликається відповідно реалізація для кожного типу
# s = Shape()                   # Викине помилку! Абстрактний клас не можна ініціалізувати.


################################## Коротка шпаргалка абстракцій
# ABC                           → базовий клас для створення абстрактних структур
# @abstractmethod               → деструктор-маркер: обов'язковий до реалізації в нащадках
# Polymorphism (Поліморфізм)    → єдиний інтерфейс (area/perimeter) для різних об'єктів


####################################################################################
# CLASSMETHODS & STATICMETHODS (методи класу та статичні методи)
####################################################################################


class UserMethods:
    __count = 0

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    # @classmethod приймає 'cls' (сам клас) замість 'self'. Спрацьовує на рівні класу.
    @classmethod
    def get_count(cls):
        return cls.__count  # Дозволяє безпечно отримати приватну змінну класу __count

    # @staticmethod — це звичайна функція, розміщена всередині класу. Не має доступу ні до self, ні до cls.
    @staticmethod
    def greeting():
        print("Hello World!")


# UserMethods.greeting()         # Виклик через назву класу
# print(UserMethods.get_count()) # Отримання приватного лічильника класу без екземпляра


################################## Коротка шпаргалка статичних методів
# @classmethod (cls)            → працює з атрибутами самого класу, викликається як Class.method()
# @staticmethod                 → утилітарна функція без доступу до стану класу чи екземпляра


####################################################################################
# DUNDER METHODS OVERLOADING (перевантаження операторів та спецметоди)
####################################################################################
from typing import Any, Self


class UserOverload:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return str(self.__dict__)

    def __repr__(self) -> str:
        return self.__str__()

    # Перевантаження оператора "+" (user1 + user2)
    def __add__(self, other: Self) -> int:
        return self.age + other.age

    # Перевантаження оператора "-" (user1 - user2)
    def __sub__(self, other: Self) -> int:
        return self.age - other.age

    # Перевантаження функції len() (len(user1))
    def __len__(self) -> int:
        return len(self.name)


# u1 = UserOverload("Max", 43)
# u2 = UserOverload("Oleg", 12)
# print(u1 + u2)                # 55 (__add__)
# print(u1 - u2)                # 31 (__sub__)
# print(len(u1))                # 3  (__len__)


################################## SINGLETON PATTERN ТА __CALL__
# Singleton гарантує, що у класу може бути ТІЛЬКИ ОДИН екземпляр в пам'яті.


class SingletonUser:
    __instance = None

    # __new__ викликається ДО __init__ і відповідає за СТВОРЕННЯ об'єкта в пам'яті
    def __new__(cls, *args: Any, **kwargs: Any) -> Self:
        if not isinstance(cls.__instance, cls):
            cls.__instance = super().__new__(cls)  # Створюється лише 1 раз
        return cls.__instance

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    # __call__ дозволяє викликати екземпляр як функцію: user(22)
    def __call__(self, value: int) -> Any:
        self.age += value


# u1 = SingletonUser("Max", 43)
# u2 = SingletonUser("Oleg", 46) # поверне ТІЙ Ж САМИЙ об'єкт, що й u1
# print(id(u1) == id(u2))        # True (однакова адреса в пам'яті)
# u1(10)                        # викликає __call__, додає 10 до age


################################## Коротка шпаргалка спеціальних методів
# __new__(cls)                  → виділення пам'яті під об'єкт (корисно для Singleton)
# __call__(self)                → дозволяє викликати екземпляр класу як функцію obj()
# __add__ / __sub__ / __len__   → перевизначення магічних операторів +, -, len()


####################################################################################
# CUSTOM CONTAINER (власний клас-масив з індексацією та ітерацією)
####################################################################################

# Клас реалізує поведінку масиву/списку через magic-методи індексації та методи обробки map/filter
from collections.abc import Callable


class Array:
    def __init__(self, *args: Any) -> None:
        self.__arr = [*args]  # Упаковка аргументів у приватний список

    def __str__(self) -> str:
        return str(self.__arr)

    def __len__(self) -> int:
        return len(self.__arr)

    # Доступ за індексом для запису: arr[0] = 5
    def __setitem__(self, key: int, value: Any) -> None:
        self.__arr[key] = value

    # Доступ за індексом для читання: print(arr[0])
    def __getitem__(self, key: int) -> Any:
        return self.__arr[key]

    # Видалення за індексом: del arr[0]
    def __delitem__(self, key: int) -> None:
        del self.__arr[key]

    def push(self, item: Any) -> None:
        self.__arr.append(item)

    # Власний метод map: повертає НОВИЙ екземпляр класу Array з трансформованими даними
    def map(self, cb: Callable[[Any], Any]) -> Self:
        return self.__class__(*[cb(item) for item in self.__arr])

    # Власний метод filter: повертає НОВИЙ екземпляр класу Array з відфільтрованими даними
    def filter(self, cb: Callable[[Any], Any]) -> Self:
        return self.__class__(*[item for item in self.__arr if cb(item)])


# ДЕМОНСТРАЦІЯ ВИКОРИСТАННЯ:
arr = Array(4, "text", 9, 3, 1, 90, 4, 34, 890)

# 1. Трансформація елементів через map (помножити числа на 2)
arr_map = arr.map(lambda x: x * 2 if isinstance(x, (int, float)) else x)
print(arr_map)

# 2. Фільтрація елементів через filter (тільки числа менше 30)
arr_filter = arr.filter(lambda x: isinstance(x, (int, float)) and x < 30)
print(arr_filter)


################################## Коротка шпаргалка спецметодів контейнерів
# __getitem__(self, key)       → читання елемента за індексом/ключем obj[key]
# __setitem__(self, key, val)  → запис значення за індексом/ключем obj[key] = val
# __delitem__(self, key)       → видалення елемента за індексом del obj[key]
