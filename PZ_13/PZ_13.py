#Вариант 31.
#1. Сгенерировать двумерный список, в которой нечетные элементы заменяются на 0.
#2. В двумерном списке элементы второго столбца заменить элементами из
#одномерного динамического массива соответствующей размерности.

import random

rows = 5
cols = 5

list1 = [[random.randint(1, 100) for _ in range(cols)] for _ in range(rows)]

list2 = [[0 if x % 2 != 0 else x for x in row] for row in list1]


dynamic_array = [random.randint(1, 100) for _ in range(rows)]

list3 = [[row[0], dynamic_array[i], *row[2:]] for i, row in enumerate(list1)]


print("Исходный список:")
for row in list1:
    print(row)

print("\nЗамена на 0:")
for row in list2:
    print(row)

print("\nДинамический массив для замены:", dynamic_array)

print("\nЗамена значений на значения динамического массива:")
for row in list3:
    print(row)