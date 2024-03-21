import subprocess
import timeit
import sys
def shellSort(a, n):
    odstep = n // 2

    while odstep > 0:
        i = odstep
        while i < n:
            temp = a[i]
            j = i
            while j >= odstep and a[j - odstep] > temp:
                a[j] = a[j - odstep]
                j -= odstep

            a[j] = temp
            i += 1
        odstep //= 2
    return a
if __name__ == "__main__":
    A = [1,23,5,1,2,4,6,7,5,234,6,7456,2678].reverse()
    shellSort(A,len(A))
    print(A)