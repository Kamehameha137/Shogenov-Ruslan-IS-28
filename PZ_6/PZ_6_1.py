#Дан целочисленный список размера N. Увеличить все четные числа, содержащиеся
#в списке, на исходное значение первого четного числа. Если четные числа в списке
#отсутствуют, то оставить список без изменений.
# Вариант 30 Номер 1

listLenght = int(input("Введите длинуу списка: "))
N = []

def listChange():
    firstEvenNum = 0

    #заполняю список длинной N
    for i in range (listLenght):
        N.append(int(input(f"Введитие {i+1} число: ")))

    print("Список: ", N)

    # для нахождения первого четного числа в списке
    for i in range(len(N)):
        if N[i] % 2 == 0:
            firstEvenNum = N[i]
            break

    print("Первое чётное число: ", firstEvenNum)

    #увеличение
    for i in range(len(N)):
        if N[i] % 2 == 0:
            N[i]+= firstEvenNum

    print("Окончательный список", N)

listChange()