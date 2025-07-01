# Вариант 31
# Из исходного текстового файла (price.txt) выбрать все цены. Посчитать количество полученных элементов.

import re

with open('/price.txt', 'r', encoding='utf-8') as file:
    content = file.read()

prices = re.compile(r'(\d+)\s*руб\.?\s*(\d+)\s*коп\.?').findall(content)

formatted_prices = [f"{rub} руб. {kop} коп." for rub, kop in prices]

print("Найденные цены:")
for price in formatted_prices:
    print(price)

print(f"\nОбщее количество цен: {len(prices)}")