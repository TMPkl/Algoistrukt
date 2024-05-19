import timeit

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
def EulerR():
    global ln
    global nv
    global wierz
    global results

    with open("./prog_for_raport/inputE.txt", "r") as file:
            firstLine = file.readline().split()
            nv = int(firstLine[0])
            ne = int(firstLine[1])
            ln = [[] for _ in range(nv)]
            for _ in range(ne):
                line = file.readline().split()
                ln[int(line[0])].append(int(line[1]))
                ln[int(line[1])].append(int(line[0]))
    wierz = []
    results = []
    t0 =timeit.default_timer()
    DFS_Euler(0)
    t1 = timeit.default_timer()
    print(t1-t0,end="\t")
    return #t1-t0+"\t"