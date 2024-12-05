#Описать функцию Minmax(X, Y), записывающую в переменную X минимальное из
#значений X и Y, а в переменную Y — максимальное из этих значений (X и Y —
#вещественные параметры, являющиеся одновременно входными и выходными).
#Используя четыре вызова этой функции, найти минимальное и максимальное из
#данных чисел A, B, C, D.

A = float(input("Pervoe chislo "))
B = float(input("Vtoroe chislo "))
C = float(input("Trerie chislo "))
D = float(input("Chetvertoe chislo "))

def Minmax(X, Y):
    maximum = max(X, Y)
    minimum = min(X, Y)

    X = minimum
    Y = maximum


    return X, Y

#сравниваю 2 пары, чтоб найти в каждой паре максимально и минимально
min1, max1 = Minmax(A, B)  
min2, max2 = Minmax(C, D)  

#беру минимально число из каждой пары и записываю меньшее в finalMin. finalMax нужна, чтобы finalMin не хранила не нужное значение
finalMin, finalMax = Minmax(min1, min2)
#беру максимальное число из каждой пары и записываю наибольшее в finalMax
finalMax = max(max1, max2)


print(f"Min: {finalMin}, Max: {finalMax}")