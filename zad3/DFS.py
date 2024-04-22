import os

def print_my_friends(node, graph):
    global visited
    if node not in visited:
        if graph[node] == []:
            print(node)
            visited.add(node)
            return
        visited.add(node)
        print(node)
        for friend in graph[node]:
            print_my_friends(friend, graph)

if __name__ == "__main__":
    nv = int(input("Number of vertices: "))
    graph = {i: [] for i in range(nv)}
    visited = set()
    # Taking input edges until "EXIT" is entered
    while True:
        line = input("Enter edge (from to), or type 'EXIT' to finish: ")
        if line == "EXIT":
            break
        # Ensure the input line contains at least two elements
        if len(line.split()) < 2:
            print("Invalid input format. Please provide an edge in the format 'from to'.")
            continue
        edge = tuple(map(int, line.split()))
        # Ensure edge tuple has two elements (from and to)
        if len(edge) != 2:
            print("Invalid input format. Please provide an edge in the format 'from to'.")
            continue
        graph[edge[0]].append(edge[1])
        os.system('cls')  # Clearing the screen (works on Windows)
        print(graph)
    
    start_node = int(input("Enter the node to start from: "))
    print_my_friends(start_node, graph)

    for node in range(nv):
        if node not in visited:
            print_my_friends(node, graph)
