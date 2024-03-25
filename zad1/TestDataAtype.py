import random
import sys
import itertools
def genA(n):

    L = [random.randrange(0,n*10) for _ in range(n//2)]
    R = [random.randrange(1,n*10) for _ in range(n-len(L))]
    
    L.sort()
    R.sort(reverse=True)


    str_from_tab = str(list(itertools.chain(L,R)))[1:-1]#.replace(",","").replace(" ","\n")


    f=open("test_data_A.txt","w")
    f.write(str_from_tab)
    f.close()
    return list(itertools.chain(L,R))
if len(sys.argv) == 2:
    genA(int(sys.argv[1]))
else:
    genA(int(input("podaj ilość danych testowych: ")))