import random
import itertools
import sys
def genV(n):

    #n= 10000 #int(input())

    L = [random.randrange(0,n*10,2) for _ in range(n//2)]
    R = [random.randrange(1,n*10,2) for _ in range(n-len(L))]
    
    L.sort()
    R.sort(reverse=True)


    str_from_tab = str(list(itertools.chain(R,L)))[1:-1]#.replace(",","").replace(" ","\n")


    f=open("test_data_V.txt","w")
    f.write(str_from_tab)
    f.close()
    return list(itertools.chain(L,R))
if len(sys.argv) == 2:
    genV(int(sys.argv[1]))
else:
    genV(int(input("podaj ilość danych testowych: ")))