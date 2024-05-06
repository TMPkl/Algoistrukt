import random

def GrafGen(n):
    #print("Test 1")
    with open("zad3/inputIN.txt", "w") as file:
        nv = n*(n-1)//8
        file.write(str(n) + " " + str(nv) + "\n")
        edges = set()
        i = 0
        #print("Generating graph with",n,"vertices")
        tried = 0
        while i < nv and tried < 500:
            tried += 1
            #print(i)
            b = random.randrange(0,n//2)
            a = random.randrange(n//2+1,n-1)
            if b != a and (a,b) not in edges and (b,a) not in edges:
                file.write(str(b) + " " + str(a) + "\n")
                edges.add((b,a))
                i += 1
                tried = 0
    #print("Generated graph with",n,"vertices")
    return