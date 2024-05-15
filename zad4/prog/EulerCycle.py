def delete_v(v):
    global ln  
    newlistofI = []
    for x in ln:
        if x.count(v) != 0:
            x.pop(x.index(v))
        newlistofI.append(x)
    ln = newlistofI

def DFS_Euler(v):
    global ln  
    for u in ln[v]:
        if u in ln[v]:
            ln[v].remove(u)
            ln[u].remove(v)
        DFS_Euler(u)
    wierz.append(v)

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

wierz = []
results = []
DFS_Euler(0)
if len(wierz) != ne+1 :
    print("brak")
else:  
    print("Euler cycle: ")
    print(wierz)
