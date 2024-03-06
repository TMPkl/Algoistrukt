import random
import itertools

n = int(input())

L = [random.randint(0,n*10) for _ in range(n//2)]
R = [random.randint(0,n*10) for _ in range(n-len(L)+1)]
5
L.sort()
R.sort(reverse=True)


str_from_tab = str(list(itertools.chain(L,R)))[1:-1].replace(",","").replace(" ","\n")


f=open("test_data_A.txt","w")
f.write(str_from_tab)
print(list(itertools.chain(L,R)))