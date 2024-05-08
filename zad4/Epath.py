def is_connected(ln, visited, v):
    visited[v] = True
    count = 1
    for i in range(len(ln)):
        if ln[v][i] and not visited[i]:
            count += is_connected(ln, visited, i)
    return count

def is_graph_connected(ln):
    nv = len(ln)
    visited = [False] * nv
    for i in range(nv):
        if sum(ln[i]) > 0:
            return is_connected(ln, visited, i) == sum(visited)
    return True

def is_in_deg(v, ln):
    line = ln[v]
    return sum(line)

import os

if __name__ == "__main__":
    choice = input("Read from file press 'F', read from console press 'C': ")
    if choice == 'F':
        with open("input.txt", "r") as file:
            firstLine = file.readline().split()
            nv = int(firstLine[0])
            ne = int(firstLine[1])
            ln = [[0] * nv for _ in range(nv)] 
            for _ in range(ne):
                line = file.readline().split()
                ln[int(line[0])][int(line[1])] = 1
                ln[int(line[1])][int(line[0])] = 1
    else:
        firstLine = input().split()
        nv = int(firstLine[0])
        ne = int(firstLine[1])
        ln = [[0] * nv for _ in range(nv)] 
        for _ in range(ne):
            line = input().split()
            ln[int(line[0])][int(line[1])] = 1
            ln[int(line[1])][int(line[0])] = 1
        os.system('cls')

    degs = [] 
    for i in range(nv):
        degs.append(is_in_deg(i, ln))
    
    n_of_odd = 0
    for i in range(nv):
        if degs[i] % 2 == 1:
            n_of_odd += 1
        if n_of_odd > 2:
            print("NO")
            break

    if n_of_odd == 0:
        if is_graph_connected(ln):
            print("Cykl Eurela")
        else:
            print("Graph is not connected, cannot form an Euler cycle.")
    elif n_of_odd == 2:
        if is_graph_connected(ln):
            print("Ścieżka Eurela")
        else:
            print("Graph is not connected, cannot form an Euler path.")
