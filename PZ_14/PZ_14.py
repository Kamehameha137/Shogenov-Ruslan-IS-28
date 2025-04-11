# Вариант 31
# Из исходного текстового файла (price.txt) выбрать все цены. Посчитать количество полученных элементов.

file = open("price.txt", 'r', encoding='utf-8').read()

prices = 0

for cop in file.split():
     if 'коп.' in cop.replace(',', ''):
          prices += 1

print(prices)
