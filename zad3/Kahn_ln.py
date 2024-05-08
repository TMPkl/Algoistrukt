import os

def deg(v,ln):
    a = 0
    line = ln[v]
    for x in line:
        if x == 1:
            a+=1
    return a


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
            ln[int(line[1])][int(line[0])] = 1

else:
    firstLine = input().split()
    nv = int(firstLine[0])
    ne = int(firstLine[1])
    ln = [[0]*nv for _ in range(nv)] 

    for _ in range(ne):
        line = input().split()
        ln[int(line[0])][int(line[1])] = 1
        ln[int(line[1])][int(line[0])] = 1
    os.system('cls')

degs = []
for v in range(nv):
    degs.append(deg(v,ln))