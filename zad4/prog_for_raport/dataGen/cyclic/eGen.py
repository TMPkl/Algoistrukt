import networkx as nx

def generate_eulers_graph(wierzcholki,nasycenie):
    G = nx.erdos_renyi_graph(wierzcholki, nasycenie)
    with open("euler_cycle.txt", "w") as file:
        file.write(f"{wierzcholki+1} {G.number_of_edges()}\n")
    with open("euler_cycle.txt", "a") as file:
        for edge in nx.eulerize(G).edges():
            file.write(f"{edge[0]} {edge[1]}\n")
    return
