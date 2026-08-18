# 1. написати прогу, яка вибирає зі введеної строки цифри і виводить їх через кому,

# наприклад:

# st = ‘as 23 fdfdg544’ введена строка

# 2,3,5,4,4 #вивело в консолі.


# st: str = "as 23 fdfdg544"

# digits = [i for i in st if i.isdigit()]
# print(",".join(digits))

# digits = []

# for i in st:
#     if i.isdigit():
#         digits.append(i)

# print(",".join(digits))


# 2)написати прогу, яка вибирає зі введеної строки числа і виводить їх так, як вони написані

# наприклад:

# st = ‘as 23 fdfdg544 34’ #введена строка

# 23, 544, 34 #вивело в консолі


# st = "as 23 fdfdg544 34"

# digits = []

# for i in st:
#     if i.isdigit():
#         digits.append(i)
#     else:
#         digits.append(" ")

# join = "".join(digits).split()

# print(*join, sep=", ")


# 1. є строка:

# greeting = "Hello, world"

# записати кожний символ, як окремий елемент списку, і зробити його заглавним:

# [‘H’, ‘E’, ‘L’, ‘L’, ‘O’, ‘,’, ‘ ‘, ‘W’, ‘O’, ‘R’, ‘L’, ‘D’]
# print(','.join([i.upper() for i in greeting]))

# 2. з діапазону від 0-50 записати тільки непарні числа, при цьому піднести їх до квадрату

# приклад:

# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, …]

# res = [i**2 for i in range(51) if i % 2 != 0]
# print(res)


# function

# – створити функцію, яка виводить List

# list = [1, 2, 3, "text", True]

# def print_list(lst):
#     print(lst)


# print_list(list)

# – створити функцію, яка приймає три числа, та виводить та повертає найбільше.

# def max_number(a, b, c):
#     mx = max(a, b, c)
#     print(mx)
#     return mx

# print(max_number(9, 1, 99))

# – створити функцію, яка приймає будь-яку кількість чисел, повертає найменше, а виводить найбільше

# numbers = [1, 4, 3, 6, 77, 0, 33, 44, -2]


# def min_max(*args):
#     print(f"Набільше: {max(args)}")
#     return min(args)


# print(f"Найменше: {min_max(*numbers)}")

# – створити функцію, яка повертає найбільше число з List

# numbers = [1, 4, 3, 6, 77, 0, 33, 44, -2]


# def max_from_list(list):
#     return max(list)


# print(max_from_list(numbers))


# – створити функцію, яка повертає найменше число з List

# numbers = [1, 4, 3, 6, 77, 0, 33, 44, -2]


# def min_from_list(list):
#     return min(list)


# print(f"Найменше: {min_from_list(numbers)}")

# – створити функцію, яка приймає List чисел та складає значення елементів List та повертає його.

# numbers = [1, 4, 3, 6, 77, 0, 33, 44, -3, -2]


# def sum_list(list):
#     return sum(list)


# print(f"Сума чисел: {sum_list(numbers)}")

# – створити функцію, яка приймає List чисел та повертає середнє арифметичне його значень.

# numbers = [1, 4, 3, 6, 77, 0, 33, 44, -3, -2, 7]


# def avg_list(list):
#     return sum(list) / len(list)


# print(avg_list(numbers))

# 1 Є list:

# list = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]

# – знайти мін. число

# print(min(list))

# – видалити усі дублікати

# print(set(list))

# – замінити кожне 4-те значення на ‘X’

list = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]

# list_copy = ["X" if (i + 1) % 4 == 0 else val for i, val in enumerate(list)]

list_copy = list.copy()

# for i, val in enumerate(list):
#     if (i + 1) % 4 == 0:
#         list_copy[i] = "X"

list_copy[3::4] = ["NEW"] * len(list_copy[3::4])

# for i in range(3, len(list_copy), 4):
#     list_copy[i] = "X"

print(list_copy)

# 2. вивести на екран пустий квадрат з “\*”, сторона якого вказана як аргумент функції

# 3. вивести табличку множення за допомогою циклу while

# 4. переробити це завдання під меню
