import random

def GrafGen(n):
    #print("Test 1")
    with open("zad3/inputIN.txt", "w") as file:
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
