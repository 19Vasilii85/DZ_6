from random import randint
mind  = int(input("Введите min число диапозона: "))
maxd= int(input("Введите max число диапозона: "))
countd = int(input("Введите кол-во чисел в диапозоне: "))
list_1 = [randint(mind, maxd) for i in range(countd)]
print(list_1)
list_2 = []
max = int(input("Введите max значение: "))
min = int(input("Введите min значение: "))
for i in range(len(list_1)):
    if min <= list_1[i] <= max:
        print(i, end=' ')