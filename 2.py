from random import *
n = 8
a = []
for i in range(8):
    a.append(randint(1, 99))
print(f'Создан список \n {a}')
print('------------')

print('Алгоритм O(3n) поиск минимального, максимального чисел и суммы элементов списка')
# O(3n) поиск минимального, максимального чисел и суммы элементов списка
mini = a[0]
maxi = a[0]
sum = 0
k = 0
for i in range(1, len(a)):
    k+=3
    sum +=a[i]
    if mini > a[i]:
        mini = a[i]
    if maxi < a[i]:
        maxi = a[i]
print(f'Максимальный - {maxi} Минимальный - {mini} Сумма - {sum}')
print('------------')

print('Алгоритм O(n*log(n)) - сориторвка методом Хаора')
# O(n*log(n))
#сориторвка методом Хаора
def quick(a):
    if len(a) <= 1:
        return a
    else:
        random_num = choice(a)
        smaller, equal, bigger = [], [], []
        for i in a:
            if i < random_num:
                smaller.append(i)
            elif i > random_num:
                bigger.append(i)
            else:
                equal.append(i)
        return quick(smaller) + equal + quick(bigger)
print(quick(a))
print('------------')

print('Алгоритм O(n!) - вычисление факториала рекурсивно')
#O(n!) вычисление факториала рекурсивно
def fac(n):
    if n == 0:
        return 1
    return fac(n-1) * n
print(fac(n))
print('------------')

print('Алгоритм O(n^3) - количество различных комбинаций из 3 цифр, входящих в диапазон от 0 до n')
#O (n^3)
d  = []
for a in range(n):
    for b in range(n):
        for c in range(n):
            d.append(str(a)+str(b)+str(c))
print(len(d))
print('----------')

print('Алгоритм O(3log(n)) - бинарный поиск 3 элементов')
# O (3 log(n))
n, a, k =int(input('количество элементов\n')), [], 0
for i in range(n):
    a.append(int(input('число\n')))
a.sort()
global_k, poisk1 = 0, []
for i in range(3):
    poisk1.append(int(input('число для поиска\n')))
print(f'{a}- основной спиок; {poisk1} - числа, поиск которых осуществляется')
for poisk in poisk1:
    b = a.copy()
    k = 0
    start, fin = 0, len(b) - 1
    while start <= fin:
        sr = (start+fin)//2
        k += 1
        global_k +=1
        if b[sr] == poisk:
            print(f'{poisk} число есть, итераций', k)
            break
        elif start == fin:
            print(f'{poisk} числа нет, итераций', k)
            break
        else:
            if poisk<b[sr]:
                fin = sr -1
            else:
                start = sr +1
print(global_k,'общее количество итераций')
print('------------')