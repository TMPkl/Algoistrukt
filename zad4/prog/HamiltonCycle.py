import os

global O 
global Path
global visited
global start

def Hamiltonian(v):
    global visited
    global Path
    O[v] = True
    visited += 1
    Path.append(v)  # Append the current node to the path
    if visited == nv and start in ln[v]:  # Check if we've visited all nodes and can return to start
        print(Path[1::] + [start])  # Print the Hamiltonian cycle
        return True
    for i in ln[v]:
        if not O[i]:
            if Hamiltonian(i):
                return True
    O[v] = False
    visited -= 1
    Path.pop()  # Remove the current node from the path if it doesn't lead to a solution
    return False

def StartAlgo():
    global visited
    global Path
    Path.append(start) 
    visited = 0
    if Hamiltonian(start):
        print("Cycle found")

choice = input("F - file, C - keyboard: ")
if choice == 'F':
    with open("input.txt", "r") as file:
            firstLine = file.readline().split()
            nv = int(firstLine[0])
            ne = int(firstLine[1])
            ln = [[] for _ in range(nv)]
            for _ in range(ne):
                line = file.readline().split()
                ln[int(line[0])].append(int(line[1]))
                ln[int(line[1])].append(int(line[0]))

else:
    firstLine = input().split()
    nv = int(firstLine[0])
    ne = int(firstLine[1])
    ln = [[] for _ in range(nv)]
    for _ in range(ne):
        line = input().split()
        ln[int(line[0])].append(int(line[1]))
        ln[int(line[1])].append(int(line[0]))

start = 0
visited = 0 
O = [False for _ in range(nv)]
Path = []
StartAlgo()
