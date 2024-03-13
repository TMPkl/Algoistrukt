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
    print(lst)
    return lst
if __name__ == "__main__":
    print("adwdawdawd")
    if len(sys.argv) == 2:
        subprocess.run(["python", "TestDataVtype.py", sys.argv[1]])              ############## zmiana algo generującego
        f = open("test_data_V.txt","r")                                        ############# zmiana pliku gdzie czytać dane
        A = f.read().replace(",","").split(" ")
        f.close()
        A = [int(x) for x in A]
        t0 =timeit.default_timer()
        quicksort_iteracyjnie(A)
        t1 = timeit.default_timer()
        
        results_m = open("quick_sort_results.txt", "a")   
        results_m.write(str(t1-t0)+"\n")
        results_m.close()
    else:
        A = input("podaj ilość danych testowych: ")          ##### jakie dane wygenerować 
        A = A.split(" ")
        A = [int(x) for x in A]
        t0 =timeit.default_timer()
        quicksort_iteracyjnie(A)
        t1 = timeit.default_timer()
        print(A)
        print(A,"\n","w czasie: ",t1-t0)
