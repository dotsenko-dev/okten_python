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
