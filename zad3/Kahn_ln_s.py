import timeit
import itertools as it
import os
import GrafGen 
def in_degree(v, listOfI):
    l = list(it.chain.from_iterable(listOfI))
    return l.count(v) 

def delete_v(v, listOfI):
    newlistofI = []
    for x in listOfI:
        if x.count(v) != 0:
            x.pop(x.index(v))
        newlistofI.append(x)
    newlistofI[v] = []
    return newlistofI
def topological_sort():
        with open("inputIN.txt", "r") as file:
            firstLine = file.readline().split()
            nv = int(firstLine[0])
            ne = int(firstLine[1])
            ln = [[] for _ in range(nv)]
            for _ in range(ne):
                line = file.readline().split()
                if line[0] == line[1]:
                    os.system('cls')
                    raise Exception('graf nie jest acykliczny')
                ln[int(line[0])].append(int(line[1]))
                
        listawyprintowanych = set()   
        t0 =timeit.default_timer()
        while any(ln):
            flag = False
            for v in range(nv):
                if in_degree(v, ln) == 0 and not v in listawyprintowanych:
                    #print(v)
                    listawyprintowanych.add(v)
                    ln = delete_v(v, ln)
                    flag = True
                    
                    break
            if not flag:
                raise Exception('graf nie jest acykliczny')
        if ln != []:
            for x in range(nv):
                if x not in listawyprintowanych:
                    #print(x)
                    listawyprintowanych.add(x)
        t1 = timeit.default_timer()
        wyniki.write(str(t1-t0) + " ")
if __name__ == "__main__":
    wyniki = open("wynikiIN.txt","w")
    for i in range(0,1000,100):
        n = 0
        print("Test n:",i)
        wyniki.write("Test n: " + str(i) + " ")
        while n < 5:
            GrafGen.GrafGen(i)
            try:
                
                topological_sort()
                print("Test",i+1,"passed")
                n+=1        
            except Exception as e:
                pass
        wyniki.write("\n")
    wyniki.close()
