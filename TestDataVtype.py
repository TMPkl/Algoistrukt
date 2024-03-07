import random
import itertools

n = int(input())

L = [random.randrange(0,n*10,2) for _ in range(n//2)]
R = [random.randrange(1,n*10,2) for _ in range(n-len(L))]
5
L.sort()
R.sort(reverse=True)


str_from_tab = str(list(itertools.chain(R,L)))[1:-1].replace(",","").replace(" ","\n")


f=open("test_data_V.txt","w")
f.write(str_from_tab)
print(list(itertools.chain(L,R)))