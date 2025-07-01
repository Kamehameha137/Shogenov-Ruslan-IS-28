#Вариант 31.
#1. Сгенерировать двумерный список, в которой нечетные элементы заменяются на 0.
#2. В двумерном списке элементы второго столбца заменить элементами из
#одномерного динамического массива соответствующей размерности.

import random

rows = 5
cols = 5

list1 = [[random.randint(1, 100) for _ in range(cols)] for _ in range(rows)]

print("Исходный список:")
for row in list1:
    print(row)

def first(list_mod):
    for i in range(len(list_mod)):
        for j in range(len(list_mod[i])):  
            if list_mod[i][j] % 2 != 0: 
                list_mod[i][j] = 0
    return list_mod

dynamic_array = [random.randint(1, 100) for _ in range(rows)]
print("\nДинамический массив для замены:", dynamic_array)

def second(list_mod):
    for i in range(len(list_mod)):
        list_mod[i][1] = dynamic_array[i]
    
    return list_mod

print("\nЗамена на 0:")
for row in first(list1):
    print(row)

print("\nЗамена значений на значения динамического массива:")
for row in second(list1):
    print(row)