import sys
import random
def genI(n):
    D = [random.randrange(0,n*10,1) for _ in range(n)]
    D.sort()
    f=open("test_data_I.txt","w")
    f.write(str(D)[1:-1])
    f.close()
    return D

if len(sys.argv) == 2:
    genI(int(sys.argv[1]))
else:
    print(genI(int(input("podaj ilość danych testowych: "))))
    

