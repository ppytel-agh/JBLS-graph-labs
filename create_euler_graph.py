# 2-4

import argparse
import random
import networkx as nx
from networkx.convert_matrix import to_numpy_array
from graphic_sequence import is_sequence_graphic
from script_common import draw_graph_on_circle

def edge_switching(G, num_swaps):
    edges = list(G.edges())
    n = len(edges)

    for _ in range(num_swaps):
        a, b = edges[random.randint(0, n - 1)]
        c, d = edges[random.randint(0, n - 1)]

        if (a == c) or (a == d) or (b == c) or (b == d):
            continue

        if not G.has_edge(a, c) and not G.has_edge(b, d):
            G.remove_edge(a, b)
            G.remove_edge(c, d)
            G.add_edge(a, c)
            G.add_edge(b, d)

def random_simple_graph_with_degrees_sequence(degrees_sequence):
    if not nx.is_graphical(degrees_sequence):
        return None

    G = nx.Graph(nx.havel_hakimi_graph(degrees_sequence))

    num_swaps = len(G.edges())
    edge_switching(G, num_swaps)

    return G

def is_valid_edge(G, u, v):
    if len(list(G.neighbors(u))) == 1:
        return True
    G.remove_edge(u, v)
    is_connected = nx.is_connected(G)
    G.add_edge(u, v)
    return is_connected

def fleury_algorithm(G, node):
    cycle = []
    for neighbor in list(G.neighbors(node)):
        if G.has_edge(node, neighbor) and is_valid_edge(G, node, neighbor):
            G.remove_edge(node, neighbor)
            cycle += fleury_algorithm(G, neighbor)
    cycle.append(node)
    return cycle

def find_eulerian_cycle(G):
    if not all(deg % 2 == 0 for _, deg in G.degree()):
        print("Not a Euler graph")
        return None

    start_node = list(G.nodes())[0]
    return fleury_algorithm(G.copy(), start_node)

def Euler(v):
    for i in range(V_size):
        while (adjacency_matrix[v][i] != 0):
            adjacency_matrix[v][i] -= 1
            adjacency_matrix[i][v] -= 1
            Euler(i)
    result.append(v)
 
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('vertex_number', type=int, nargs=1)
    args = parser.parse_args()
    V_size = args.vertex_number[0]

    if V_size > 2:
        max_graph_degree = (V_size - 1) // 2
        graph = []
        for i in range(V_size):
            graph.append(random.randint(1, max_graph_degree) * 2)
        while(not is_sequence_graphic(graph)):
            graph.clear()
            for i in range(V_size):
                graph.append(random.randint(1, max_graph_degree) * 2)
        print(graph)
        nx_graph = random_simple_graph_with_degrees_sequence(graph)
        is_connected = nx.is_connected(nx_graph)
        while not is_connected:
            nx_graph = random_simple_graph_with_degrees_sequence(graph)
            is_connected = nx.is_connected(nx_graph)
        result = []
        adjacency_matrix = to_numpy_array(nx_graph)
        Euler(0)
        print("Euler cycle:", result)
        draw_graph_on_circle(nx_graph)

    else:
        print("Graph must have at least 3 vertices")