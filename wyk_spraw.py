from merge_sort import mergeSort
from quick_sort import *
from shellSort import shellSort
import matplotlib.pyplot as plt
import random
import itertools
import numpy as np
import timeit
def genV(n):

    L = [random.randrange(0,n*10,2) for _ in range(n//2)]
    R = [random.randrange(1,n*10,2) for _ in range(n-len(L))]
    
    L.sort()
    R.sort(reverse=True)

    return list(itertools.chain(L,R))

def genD(n):
    D = [random.randrange(0,n*10,1) for _ in range(n)]
    D.sort(reverse=True)
    f=open("test_data_D.txt","w")
    f.write(str(D)[1:-1])
    f.close()
    return D

def genA(n):

    L = [random.randrange(0,n*10) for _ in range(n//2)]
    R = [random.randrange(1,n*10) for _ in range(n-len(L))]
    
    L.sort()
    R.sort(reverse=True)

    return list(itertools.chain(L,R))

def genR(n):
    D = [random.randrange(0,n*10) for _ in range(n)]
    f=open("test_data_R.txt","w")
    f.write(str(D)[1:-1])
    f.close()
    return D

def genI(n):
    D = [random.randrange(0,n*10,1) for _ in range(n)]
    D.sort()
    f=open("test_data_I.txt","w")
    f.write(str(D)[1:-1])
    f.close()
    return D


number_of_tests = 10   #ilośc testów na podstawie jakiej wykonuje obliczenia
number_of_numbers = np.linspace(1,1000,15)  #liczba liczb do posortowania--- N
xs = []
ys = []

xq = []
yq = []

xm = []
ym = []

for rown in range(15):
    test_data = genA(int(number_of_numbers[rown]))

    t0 =timeit.default_timer()
    shellSort(test_data,len(test_data))
    t1 = timeit.default_timer()
    ys.append(t1-t0)

    t0 =timeit.default_timer()
    quicksort_iteracyjnie(test_data)
    t1 = timeit.default_timer()
    yq.append(t1-t0)

    t0 =timeit.default_timer()
    mergeSort(test_data)
    t1 = timeit.default_timer()
    ym.append(t1-t0)

    xs.append(number_of_numbers[rown])
    xq.append(number_of_numbers[rown])
    xm.append(number_of_numbers[rown])

plt.plot(xs, ys, color='#FF0000', linestyle='dashed', label='shell sort',linewidth = 2,
         marker='o', markersize=7) 
plt.plot(xq, yq, color='#00FF00', linestyle='dashed',label='quick sort',linewidth = 2,
         marker='o',  markersize=7) 
plt.plot(xm, ym, color='#0000FF',linestyle='dashed', label='merge',linewidth = 2,
         marker='o',  markersize=7)

plt.xlabel('number of numbers to sort')
plt.ylabel("avg timge required to sort  [seconds]")
plt.title('shell sort')
plt.legend()
plt.show()