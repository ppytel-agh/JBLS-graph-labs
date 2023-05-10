# 2-6

import networkx as nx
from script_common import draw_graph_on_circle

def hamiltonian_cycle(G, path):
    if len(path) == len(G):
        if path[0] in G.neighbors(path[-1]):
            return path + [path[0]]
        else:
            return None

    for node in G.neighbors(path[-1]):
        if node not in path:
            path.append(node)
            cycle = hamiltonian_cycle(G, path)
            if cycle:
                return cycle
            path.pop()

    return None

def find_hamiltonian_cycle(G):
    for node in G.nodes():
        path = [node]
        cycle = hamiltonian_cycle(G, path)
        if cycle:
            return cycle

    return None

# G = nx.Graph([
# (0, 1), (1, 2), (2, 0), (0, 3), (1, 3), (2, 3)
# ])  # K4
G = nx.Graph([
    (0, 1), (1, 2), (2, 3), (3, 4), (4, 0)  # C5
])
# G = nx.Graph([
#     (0, 1), (1, 2), (2, 3), (3, 4)
# ])

cycle = find_hamiltonian_cycle(G)

if cycle:
    print("Hamiltonian cycle exists:", cycle)
    draw_graph_on_circle(G)
else:
    print("Hamiltonian cycle does not exists")
