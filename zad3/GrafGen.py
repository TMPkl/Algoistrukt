import random

def GrafGen(n):
    with open("inputIN.txt", "w") as file:
        nv = n*(n-1)//4
        file.write(str(n) + " " + str(nv) + "\n")
        edges = set()
        i = 0
        while i < nv:
            b = random.randrange(0,n//2)
            a = random.randrange(n//2+1,n-1)
            if b != a and (a,b) not in edges and (b,a) not in edges:
                file.write(str(b) + " " + str(a) + "\n")
                edges.add((b,a))
                i += 1
    #print("Generated graph with",n,"vertices")
    file.close()
    return