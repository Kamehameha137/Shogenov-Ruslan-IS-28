# Вариант 31
# Из исходного текстового файла (price.txt) выбрать все цены. Посчитать количество полученных элементов.

file = open("price.txt", 'r')

prices = 0

print(file.read().split())
