import sys
import random
def genD(n):
    D = [random.randrange(0,n*10,1) for _ in range(n)]
    D.sort(reverse=True)
    f=open("test_data_D.txt","w")
    f.write(str(D)[1:-1])
    f.close()
    return D

if len(sys.argv) == 2:
    genD(int(sys.argv[1]))32
else:
    print(genD(int(input("podaj ilość danych testowych: "))))
    

