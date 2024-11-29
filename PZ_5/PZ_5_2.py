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
    maximum = max(A, B, C, D)
    minimum = min(A, B, C, D)

    X = minimum
    Y = maximum

    print("Минимум:", X)
    print("Максимум:", Y)

    return X, Y

Minmax()
