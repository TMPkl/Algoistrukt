import subprocess as sbp
f = open("merge_sort_results.txt","w")
f.close()

number_of_tests = 5   #ilośc testów na podstawie jakiej wykonuje obliczenia
number_of_numbers = 10  #liczba liczb do posortowania
for _ in range(number_of_tests):
    sbp.call(["python","merge_sort.py",str(number_of_numbers)])