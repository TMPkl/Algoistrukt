import itertools as it
import os
def is_in_deg(v,ln):
    line = ln[v]
    for x in line:
        if x == -1:
            return 1
    return 0

def delConnection(v,ln):
    ln[v] = [0]*len(ln)
    for x in range(len(ln)):
        ln[x][v] = 0
    return

if __name__ == "__main__":
    choice = input("Read from file press 'F', read from console press 'C': ")
    if choice == 'F':
        with open("zad3/inputMS.txt", "r") as file:
            firstLine = file.readline().split()
            nv = int(firstLine[0])
            ne = int(firstLine[1])
            ln = [[0]*nv for _ in range(nv)] 
            for _ in range(ne):
                line = file.readline().split()
                ln[int(line[0])][int(line[1])] = 1
                ln[int(line[1])][int(line[0])] = -1

    else:
        firstLine = input().split()
        nv = int(firstLine[0])
        ne = int(firstLine[1])
        ln = [[0]*nv for _ in range(nv)] 

        for _ in range(ne):
            line = input().split()
            ln[int(line[0])][int(line[1])] = 1
            ln[int(line[1])][int(line[0])] = -1
        os.system('cls')
    flag = 1    
    was_printed = set()
    while any(it.chain.from_iterable(ln)):
        flag = -1 
        for v in range(nv):
            if is_in_deg(v,ln) == 0 and  not v in was_printed:
                if list(it.chain.from_iterable(ln)).count(1) == 1:
                    print(v,ln)
                    for x in range(len(ln[v])):
                        if ln[v][x] == 1:
                            print(x)
                            break
                        flag = 1
                    break                      
                flag = 0
                
                print(v,ln)
                delConnection(v,ln)
                was_printed.add(v)
                input()
                break
        if flag == -1:
            os.system('cls')
            raise Exception('graf nie jest acykliczny')
        if flag == 1:
            break