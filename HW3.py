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


rect1 = Rectangle(3, 7)
rect2 = Rectangle(5, 8)

print("Сума площ: ", rect1 + rect2)
print("Різниця площ: ", rect1 - rect2)
print("Порівняння площі: ", rect1 != rect2)
print("Чи один квадрат більший за інший: ", rect1 > rect2)
print("Периметр квадрату: ", len(rect1))
