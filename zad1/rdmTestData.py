import sys
import random
def genR(n):
    D = [random.randrange(0,n*10) for _ in range(n)]
    f=open("test_data_R.txt","w")
    f.write(str(D)[1:-1])
    f.close()
    return D

if len(sys.argv) == 2:
    genR(int(sys.argv[1]))
else:
    print(genR(int(input("podaj ilość danych testowych: "))))
    

