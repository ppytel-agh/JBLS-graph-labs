# 3-1

import random
import networkx as nx
import matplotlib.pyplot as plt

def generate_connected_random_graph(n, density):
    V = list(range(n))
    E = set()
    
    for i in range(1, n):
        u, v = i, random.randint(0, i - 1)
        E.add((u, v) if u < v else (v, u))
    
    max_edges = n * (n - 1) // 2
    num_edges_to_add = int((density * max_edges - len(E)))

    while len(E) < num_edges_to_add + n - 1:
        u, v = random.sample(V, 2)
        if u != v:
            edge = (u, v) if u < v else (v, u)
            if edge not in E:
                E.add(edge)
    
    weighted_edges = [(u, v, random.randint(1, 10)) for u, v in E]
    
    return V, weighted_edges

def create_networkx_graph(V, E):
    G = nx.Graph()
    G.add_nodes_from(V)
    G.add_weighted_edges_from(E)
    return G

def plot_graph_weights(G):
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=1000, font_size=12)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=12)
    plt.show()

def create_graph_weights(n, density):
    V, E = generate_connected_random_graph(n, density)
    G = create_networkx_graph(V, E)
    return G

if __name__ == "__main__":
    n = 5
    density = 0.6
    V, E = generate_connected_random_graph(n, density)
    G = create_networkx_graph(V, E)
    plot_graph_weights(G)
