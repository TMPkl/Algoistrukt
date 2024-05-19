import networkx as nx
import random

def generate_hamiltonian_graph(num_nodes, wypelnienie):
    G = nx.Graph()
    
    nodes = list(range(num_nodes))
    random.shuffle(nodes) 

    # Add edges to form a cycle
    for i in range(num_nodes):
        G.add_edge(nodes[i], nodes[(i + 1) % num_nodes])
    
   
    num_extra_edges = (int(wypelnienie * num_nodes * (num_nodes - 1) / 2) - num_nodes)%num_nodes
    potential_edges = [(u, v) for u in nodes for v in nodes if u < v and not G.has_edge(u, v)]

    extra_edges = random.sample(potential_edges, num_extra_edges)
    G.add_edges_from(extra_edges)
    with open("hamilt_cycle.txt", "w") as file:
        file.write(f"{num_nodes+1} {G.number_of_edges()}\n")
    with open("hamilt_cycle.txt", "a") as file:
        for edge in G.edges():
            file.write(f"{edge[0]} {edge[1]}\n")
    return 
generate_hamiltonian_graph(100, 0.5)