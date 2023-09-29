# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

n_set_1 = int(input("Введите кол-во элементов первого множества: "))
m_set_2 = int(input("Введите кол-во элементов второго множества: "))
set_1 = {""}
set_1.remove("")
print("Введите элементы первого множества: ")
for i in range(n_set_1):
    k = int(input())
    set_1.add(k)
set_2 = {""}
set_2.remove("")
print("Введите элементы второго множества: ")
for i in range(m_set_2):
    k = int(input())
    set_2.add(k)
inter = set_1.intersection(set_2)
set(inter)
print(inter)

# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. 
# Она растёт на круглой грядке, причём кусты высажены только по окружности. 
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное 
# число ягод — на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
# Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает 
# ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход 
# собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.

import random
N = random.randint(3, 9)
print(f"Всего на грядке растет {N} кустов")
list_1 = []
for i in range(N):
    list_1.append(random.randint(20, 100))
print(list_1)
k = 0
sum = 0
max = sum
i = 0
while i < (N - 1):
    sum = list_1[k] + list_1[k - 1] + list_1[k + 1]
    if sum > max:
        max = sum
    i = i + 1
    k += 1
    print(sum)
sum = list_1[N - 1] + list_1[0] + list_1[N - 2]
print(sum)
if sum > max:
    max = sum
print(f"Максимального числа ягод, которое может собрать за один заход собирающий модуль равно: {max}")


