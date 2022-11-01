from random import *
from timeit import *
n = 8
A = []
for i in range(8):
    A.append(randint(1, 99))
print(A)
print('------------')
B = A.copy()
#создание готового списка
start = default_timer()
for i in range(0, n-1):
    for j in range(0, n-1):
        if A[j] > A[j + 1]:
            A[j], A[j + 1] = A[j + 1], A[j]
print(A)
time1 = default_timer() - start
print('Время пузырьковой сортировки:', time1)

start = default_timer()
B.sort()
time2 = default_timer() - start
print(B)
print('Время sort:', time2)
print(time1>time2)
