#Составить функцию, которая выполнит суммирования числового ряда
# n + 1 (для примера)
import math


def Summa():
    endLim = int(input("Введите кол-во суммирований"))
    n = int(input("Введите точку отчёта"))

    result = 0

    for i in range(endLim):
        print("n = ", n)
        result += n+1 #вместо n + 1 любая формула. Например (n**2)/2 или (n**10)/(n**3)
        n += 1
        

    print("Result", result)

Summa()