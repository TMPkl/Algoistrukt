import random
import itertools
def genA():

    n= 10000 #int(input())
    L = [random.randrange(0,n*10,2) for _ in range(n//2)]
    R = [random.randrange(1,n*10,2) for _ in range(n-len(L))]
    
    L.sort()
    R.sort(reverse=True)


    str_from_tab = str(list(itertools.chain(L,R)))[1:-1].replace(",","")


    f=open("test_data_A.txt","w")
    f.write(str_from_tab)
    f.close()
    return list(itertools.chain(L,R))
genA()