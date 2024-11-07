'''
Вар 31 номер 2
Даны три числа. Найти сумму двух наибольших из них.
'''
a = int(input("Введите число a: "))
b = int(input("Введите число b: "))
c = int(input("Введите число c: "))

summ = a+b+c
minimal = min(a,b,c)

result = summ - minimal
print("Сумма двух наибольших чисел: ", result)