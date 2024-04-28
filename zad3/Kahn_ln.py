import itertools as it
import os

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

if __name__ == "__main__":
    choice = input("Read from file press 'F', read from console press 'C': ")
    if choice == "F":
        with open("zad3/inputIN.txt", "r") as file:
            firstLine = file.readline().split()
            nv = int(firstLine[0])
            ne = int(firstLine[1])
            ln = [[] for _ in range(nv)]
            for _ in range(ne):
                line = file.readline().split()
                if line[0] == line[1]:
                    os.system('cls')
                    print("graf cykliczny -> niemożliwe jest wykonania sortowania")
                    os.system('pause')
                    break
                ln[int(line[0])].append(int(line[1]))
            print(ln)
            
    else:
        firstLine = input().split()
        nv = int(firstLine[0])
        ne = int(firstLine[1])
        ln = [[] for _ in range(nv)]
        for _ in range(ne):
            line = input().split()
            if line[0] == line[1]:
                    os.system('cls')
                    print("graf cykliczny -> niemożliwe jest wykonania sortowania")
                    os.system('pause') 
            ln[int(line[0])].append(int(line[1]))
        os.system('cls')
    listawyprintowanych = set()
    print(ln)    
    while any(ln):
        flag = False
        for v in range(nv):
            if in_degree(v, ln) == 0 and not v in listawyprintowanych:
                print(v)
                listawyprintowanych.add(v)
                ln = delete_v(v, ln)
                flag = True
                
                break
        if not flag:
            print("graf cykliczny -> niemożliwe jest wykonania sortowania")
            os.exit()
    if ln != []:
        for x in range(nv):
            if x not in listawyprintowanych:
                print(x)
                listawyprintowanych.add(x) 