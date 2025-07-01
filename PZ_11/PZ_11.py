#Вариант 31.
#1. Средствами языка Python сформировать два текстовых файла (.txt), содержащих по одной
#последовательности из целых положительных и отрицательных чисел. Сформировать
#новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
#обработку элементов

#Элементы первого и второго файлов:
#Количество элементов первого и второго файлов:
#Элементы первой трети:
#Минимальный элемент первой трети:

import random

def generate_numbers(length):
    return [random.randint(-100, 100) for _ in range(length)]

def write_to_file(filename, sequence):
    with open(filename, 'w') as f:
        f.write(' '.join(map(str, sequence)))

def read_from_file(filename):
    with open(filename, 'r') as f:
        content = f.read()
        return list(map(int, content.split()))

nums1 = generate_numbers(15) 
nums2 = generate_numbers(15)  

write_to_file('file1.txt', nums1)
write_to_file('file2.txt', nums2)

numbers1 = read_from_file('file1.txt')
numbers2 = read_from_file('file2.txt')


def get_first_third(sequence):
    third = len(sequence) // 3
    return sequence[:third]

first_third1 = get_first_third(numbers1)
first_third2 = get_first_third(numbers2)

min_first_third1 = min(first_third1) if first_third1 else None
min_first_third2 = min(first_third2) if first_third2 else None

output_content = f"""Элементы первого и второго файлов:
{numbers1}
{numbers2}

Количество элементов первого и второго файлов:
{len(numbers1)} и {len(numbers2)}

Элементы первой трети первого файла:
{first_third1}

Элементы первой трети второго файла:
{first_third2}

Минимальный элемент первой трети первого файла: {min_first_third1}
Минимальный элемент первой трети второго файла: {min_first_third2}
"""

with open('result.txt', 'w', encoding='utf-8') as f:
    f.write(output_content)

print("Файлы успешно созданы и обработаны.")