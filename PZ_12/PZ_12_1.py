#Вариант 31.
#1. Организовать и вывести последовательность на N произвольных целых
#элементов, сформировать новую последовательность куда поместить квадраты четных
#элементов, найти их сумму и среднее арифметическое.
#2. Из заданной строки отобразить только символы нижнего регистра.
#Использовать библиотеку string. Строка 'In PyCharm, you can specify third-party standalone
#applications and run them as External Tools'.
import random

posledovatelnost = [random.randint(1, 100) for _ in range(15)]

print(f"Первая последовательность: {posledovatelnost}")

new_posledovatelnost = [x**2 for x in posledovatelnost if x % 2 == 0]

print(f"Вторая последовательность: {new_posledovatelnost}")