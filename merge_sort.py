import timeit
import subprocess
def mergeSort(lst):
    counter = 0
    if len(lst) > 1:

        pivot = len(lst) // 2

        L = lst[:pivot]
        R = lst[pivot:]

        mergeSort(L)
        mergeSort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                lst[k] = L[i]
                i += 1
            else:
                lst[k] = R[j]
                j += 1
            k += 1
        counter+=1

        while i < len(L):
            lst[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            lst[k] = R[j]
            j += 1
            k += 1
            
    return lst


f = open("test_data_A.txt","r")

A = f.read().replace(",","").split(" ")
f.close()
A = [int(x) for x in A]
t0 =timeit.default_timer()
mergeSort(A)
t1 = timeit.default_timer()
results_m = open("merge_sort_results.txt", "a")
results_m.write(str(t1-t0)+"\n")
print(t1-t0)
subprocess.run(["python", "TestDataAtype.py"])
