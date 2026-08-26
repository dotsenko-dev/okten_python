# Створити клас Rectangle:

# -він має приймати дві сторони x,y

# Описати поведінку арифметичним методом:

# - сума площин двох екземплярів класу

# – різниця площин двох екземплярів класу

# == площин на рівність

# != площин на нерівність

# > , < менше більше

# при виклику метода len() підраховувати суму сторін

from typing import Self


class Rectangle:
    # __init__ -> Initialization (Ініціалізація / Створення об'єкта)
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def area(self) -> int:
        return self.x * self.y

    # __add__ -> Addition (Додавання: +)
    def __add__(self, other: Self) -> int:
        return self.area() + other.area()

    # __sub__ -> Subtraction (Віднімання: -)
    def __sub__(self, other: Self) -> int:
        return self.area() - other.area()

    # __eq__ -> Equals (Рівно: ==)
    def __eq__(self, other: object) -> bool:
        if isinstance(other, Rectangle):
            return self.area() == other.area()
        return False

    # # __ne__ -> Not Equal (Не рівно: !=)
    # def __ne__(self, other: object) -> bool:
    #     return not self.__eq__(other)

    # __gt__ -> Greater Than (Більше ніж: >)
    def __gt__(self, other: Self) -> bool:
        return self.area() > other.area()

    # # __lt__ -> Less Than (Менше ніж: <)
    # def __lt__(self, other: Self) -> bool:
    #     return self.area() < other.area()

    # __len__ -> Length (Довжина: len())
    def __len__(self) -> int:
        return (self.x + self.y) * 2


# rect1 = Rectangle(3, 7)
# rect2 = Rectangle(5, 8)

# print("Сума площ: ", rect1 + rect2)
# print("Різниця площ: ", rect1 - rect2)
# print("Порівняння площі: ", rect1 != rect2)
# print("Чи один квадрат більший за інший: ", rect1 > rect2)
# print("Периметр квадрату: ", len(rect1))


# створити клас Human (name, age)

# створити два класи Prince и Cinderella, які наслідуються від Human:

# у попелюшки має бути ім’я, вік, розмір ноги

# у принца має бути ім’я, вік, та розмір знайденого черевичка, а також метод, котрий буде приймати список попелюшок, та шукати ту саму

# в класі попелюшки має бути count, який буде зберігати кількість створених екземплярів класу

# також має бути метод класу, який буде виводити це значення


class Human:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


class Cinderella(Human):
    count = 0

    def __init__(self, name: str, age: int, foot_size: int) -> None:
        super().__init__(name, age)
        self.foot_size = foot_size

        Cinderella.count += 1

    @classmethod
    def get_count(cls) -> int:
        return cls.count


class Prince(Human):
    def __init__(self, name: str, age: int, shoe_size: int) -> None:
        super().__init__(name, age)
        self.shoe_size = shoe_size

    def find_cinderella(self, cinderellas: list[Cinderella]) -> list[Cinderella]:
        return [c for c in cinderellas if c.foot_size == self.shoe_size]


# print(Cinderella.get_count())

cinderellas = [
    Cinderella("Avrora", 99, 34),
    Cinderella("Merry", 18, 45),
    Cinderella("Petro", 19, 38),
    Cinderella("Oksanf", 28, 27),
    Cinderella("Nastya", 58, 34),
]

# print(Cinderella.get_count())

prince = Prince("Pedro", 45, 37)

results = prince.find_cinderella(cinderellas)

if results:
    for result in results:
        print(f"Ім'я: {result.name}, вік: {result.age}")
else:
    print("not found")
