# Вариант 30 Номер 1
# Дано целое число N (>0). 
# Найти значение выражения 1.1 - 1.2 + 1.3 - ... (N слагаемых,знаки чередуются). 
# Условный оператор не использовать.

def findNum(Number):

    result = 0 # переменная для сохраниения результата

    for i in range(1, Number + 1):
        desyatki = 1 + (i/10) # число после запятой
        znaki = -1 ** (i+1) # знак действия
        result += desyatki * znaki
        
        #print("Десятки: ",desyatki, "знаки: ", znaki, "результат:", result) #проверка
    print(result)

while True:
    N = int(input("Введите значение N > 0: "))
    if N > 0:
        findNum(N)
        break
    else:
        print("Пожалуйста, введите число больше 0.")
        continue