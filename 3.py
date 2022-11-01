from matplotlib import pyplot as p
from math import log2
def logn(n):
    count=0
    for i in range(round(log2(n))):
        count+=1
    return count
def _2n(n):
    count=0
    for i in range(2**n):
        count+=1
    return count
def n2(n):
    count =0
    for i in range(n):
        for j in range(n):
            count+=1
    return count

x, y, y1, y2, y3 = [], [], [], [], []
for n in range(1, 6):
    x.append(n)
    y.append(1)
    y1.append(logn(n))
    y2.append(n2(n))
    y3.append(_2n(n))
p.plot(x, y, 'b', label = 'O(1)')
p.plot(x, y1, 'g', label = 'O(log(n))')
p.plot(x, y2, 'r', label = 'O(n^2)')
p.plot(x, y3, 'y', label = 'O(2^n')
p.ylabel('Кол-во шагов')
p.xlabel('Кол-во элементов')
p.legend()
p.grid()
p.show()
