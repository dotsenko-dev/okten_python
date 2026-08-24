"""
BE. Python core. task 2

1. написати функцію (notebook) на замикання, котра буде в собі зберігати список справ, вам потрібно реалізувати два методи:

– перший записує в список нову справу

– другий повертає всі записи

<!-- def notebook():
    todo_list = []

    def add_todo(todo):
        pass

    def get_all():
        pass

    return ... -->

2. протипізувати перше завдання
"""

# from collections.abc import Callable

# NotebookType = tuple[Callable[[str], None], Callable[[], list[str]]]


# def notebook() -> NotebookType:
#     todo_list: list[str] = []

#     def add_todo(todo: str) -> None:
#         todo_list.append(todo)

#     def get_all() -> list[str]:
#         return todo_list.copy()

#     return add_todo, get_all


# add_todo, get_all = notebook()

# add_todo("Варення")
# add_todo("Соус")

# print(get_all())

# add_todo("Перевірка")

# print(get_all())

"""
3. створити функцію, котра буде повертати суму розрядів числа у вигляді строки (також використовуємо типізацію)

Приклад:

expanded_form(12) # return ’10 + 2′

expanded_form(42) # return ’40 + 2′

expanded_form(70304) # return ‘70000 + 300 + 4’
"""


# def expanded_form(num: int) -> str:
#     s = str(num)
#     l = len(s)

#     return ", ".join([d + "0" * (l - 1 - i) for i, d in enumerate(s) if d != "0"])


# print(expanded_form(4078301))

"""
4. створити декоратор, котрий буде підраховувати, скільки разів була запущена функція, продекорована цим декоратором, та буде виводити це значення після виконання функцій

<!-- @decor
def func1():
    print("func1")

@decor
def func2():
    print("func2")

func1()
func1()
func2()
func1() -->
"""

# from collections.abc import Callable
# from typing import Any


# def decor(func: Callable[..., Any]) -> Callable[..., Any]:
#     count = 0

#     def inner(*args: Any, **kwargs: Any) -> Any:
#         nonlocal count
#         count += 1

#         result = func(*args, **kwargs)
#         print(f"{func.__name__} - {count}")

#         return result

#     return inner


# @decor
# def func_1() -> None:
#     pass


# @decor
# def func_2() -> None:
#     pass


# func_1()
# func_1()
# func_2()
# func_1()
# func_1()
# func_2()
