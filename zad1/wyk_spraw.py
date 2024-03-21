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
number_of_numbers = np.linspace(100,1000,15)  #liczba liczb do posortowania--- N
xs = []
ys = []

xq = []
yq = []

xm = []
ym = []

for generator in [genA,genD,genI,genR,genV]:
    t0 = []
    t1 = []
    xm = []
    xq = []
    xs = []
    ym = []
    ys = []
    yq = []
    eq = []
    em = []
    es = []
    print("początek generatora: "+str(generator).split()[1])
    for rown in range(15):
        srecord=[]
        qrecord = []
        mrecord = []
        for test in range(15):
            test_data = generator(int(number_of_numbers[rown]))

            t0 =timeit.default_timer()
            shellSort(test_data,len(test_data))
            t1 = timeit.default_timer()
            srecord.append(t1-t0)

            t0 =timeit.default_timer()
            quicksort_iteracyjnie(test_data)
            t1 = timeit.default_timer()
            qrecord.append(t1-t0)

            t0 =timeit.default_timer()
            mergeSort(test_data)
            t1 = timeit.default_timer()
            mrecord.append(t1-t0)

        srecord = np.array(srecord)
        qrecord = np.array(qrecord)
        mrecord = np.array(mrecord)


        yq.append(float(np.average(qrecord)))
        eq.append(float(np.std(qrecord)))

        ys.append(float(np.average(srecord)))
        es.append(float(np.std(srecord)))

        ym.append(float(np.average(mrecord)))
        em.append(float(np.std(mrecord)))

        xs.append(number_of_numbers[rown])
        xq.append(number_of_numbers[rown])
        xm.append(number_of_numbers[rown])

    #plt.errorbar(x, y, e, linestyle='None', marker='^')
    plt.errorbar(xs, ys,es ,color='#FF0000',label='shell sort',
            marker='^',) 
    plt.errorbar(xq, yq,eq, color='#00FF00',label='quick sort',
            marker='^',) 
    plt.errorbar(xm, ym,em, color='#0000FF',label='merge',
            marker='^')

    plt.xlabel('number of numbers to sort')
    plt.yscale("log")
    plt.ylabel("avg timge required to sort  [seconds]")
    plt.title(str(generator).split()[1])
    plt.legend()
    plt.savefig("plots/gen/"+str(generator).split()[1]+".png")
    plt.cla()