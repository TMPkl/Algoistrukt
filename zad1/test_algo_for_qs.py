import subprocess as sbp
import numpy as np
import matplotlib.pyplot as plt

number_of_tests = 10   #ilośc testów na podstawie jakiej wykonuje obliczenia
number_of_numbers = np.linspace(1,1000,15)  #liczba liczb do posortowania--- N
x = []
y = []

for tests in range(15):
    f = open("quick_sort_results.txt","w")
    f.close()
    for _ in range(number_of_tests):
        sbp.call(["python","quick_sort.py",str(int(number_of_numbers[tests]))])
    f = open("quick_sort_results.txt","r")
    data = [float(x.rstrip("\n")) for x in f.readlines()]
    f.close()
    d = np.array(data)
    y.append(np.average(d[1:-1]))
    x.append(number_of_numbers[tests])
f = open("zapisXiYdlajednegocalegowykresu.txt","a")
f.write(str(list(zip(x,y)))+" V"+"\n")
f.close()
plt.plot(x, y, color='green', linestyle='dashed', linewidth = 2,
         marker='o', markerfacecolor='blue', markersize=7)
plt.ylim(min(y),max(y))
plt.xlim(min(number_of_numbers),max(number_of_numbers))
plt.xlabel('number of numbers to sort')
plt.ylabel("avg timge required to sort  [seconds]")
plt.title('quick sort with data I-type')
plt.show()