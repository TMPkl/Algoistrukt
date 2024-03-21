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

if len(sys.argv) == 2:
    subprocess.run(["python", "generatives\decTestData.py", sys.argv[1]])              ############## zmiana algo generującego
    f = open("test_data_D.txt","r")                                        ############# zmiana pliku gdzie czytać dane
    A = f.read().replace(",","").split(" ")
    f.close()
    A = [int(x) for x in A]
    t0 =timeit.default_timer()
    shellSort(A)
    t1 = timeit.default_timer()
    results_m = open("quick_sort_results.txt", "a")   
    results_m.write(str(t1-t0)+"\n")
    results_m.close()
else:
    A = input("podaj ilość danych testowych: ")          ##### jakie dane wygenerować 
    A = A.split(" ")
    A = [int(x) for x in A]
   
    t0 =timeit.default_timer()
    shellSort(A,len(A))
    t1 = timeit.default_timer()
    print(A,"\n","w czasie: ",t1-t0)
