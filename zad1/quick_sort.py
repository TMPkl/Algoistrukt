import subprocess
import timeit
import sys
def podzial(lst, first, last):
    pivot = lst[last]
    i = first - 1
    for j in range(first, last):
        if lst[j] <= pivot:
            i += 1
            lst[i], lst[j] = lst[j], lst[i]
    lst[i + 1], lst[last] = lst[last], lst[i + 1]
    return i + 1

def quicksort_iteracyjnie(lst):
    if len(lst) <= 1:
        return lst

    stos = [(0, len(lst) - 1)]
    while stos:
        first, last = stos.pop()
        if first < last:
            pi = podzial(lst, first, last)
            stos.append((first, pi - 1))
            stos.append((pi + 1, last))

    return lst
if __name__ == "__main__":
    A = [10,20,30,1,3,5,6,26,77,4,1]
    quicksort_iteracyjnie(A)
    print(A)
