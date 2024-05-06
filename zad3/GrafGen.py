import random

def GrafGen(n):
    #print("Test 1")
    with open("zad3/inputIN.txt", "w") as file:
<<<<<<< HEAD
        file.write(str(n) + " " + str(n*(n-1)//6) + "\n")
        edges = set()
        nodes = list(range(n))
        
        # Generate a random directed acyclic graph
        for _ in range(n*(n-1)//6):
            edge_added = False
            attempts = 0
            while not edge_added and attempts < 10:  # Limit the number of attempts
                a = random.choice(nodes)
                b = random.choice(nodes)
                if a != b and (a, b) not in edges and not forms_cycle(edges, a, b):
                    file.write(str(a) + " " + str(b) + "\n")
                    edges.add((a, b))
                    edge_added = True
                attempts += 1
            if attempts >= 10:
                break  # If unable to add edge after 100 attempts, break

def forms_cycle(edges, a, b):
    visited = set()
    stack = [a]
    while stack:
        node = stack.pop()
        if node == b:
            return True
        if node not in visited:
            visited.add(node)
            stack.extend(neighbors(edges, node))
    return False

def neighbors(edges, node):
    return [edge[1] for edge in edges if edge[0] == node]

if __name__ == "__main__":
    GrafGen(10)
=======
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
>>>>>>> 93fa02805906f3d591b2fc8ba4be8abbfbd4054e
