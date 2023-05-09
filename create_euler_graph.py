# 2-4

import argparse
import random
import networkx as nx
from graphic_sequence import is_sequence_graphic, create_graph_from_sequence
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

def is_bridge(G, u, v):
    if G.number_of_edges(u, v) > 1:
        return False
    original_degree = {node: G.degree(node) for node in G.neighbors(u)}
    G.remove_edge(u, v)
    visited = set()
    dfs(u, G, visited)
    is_bridge = len(visited) != sum(original_degree.values()) // 2
    G.add_edge(u, v)
    return is_bridge

def dfs(node, G, visited):
    visited.add(node)
    for neighbor in G.neighbors(node):
        if neighbor not in visited:
            dfs(neighbor, G, visited)

def find_euler_cycle(G):
    start_node = max(G.nodes(), key=lambda node: G.degree(node))

    euler_path = []
    current_node = start_node

    while len(G.edges()) > 0:
        next_node = None
        neighbors = list(G.neighbors(current_node))
        for neighbor in neighbors:
            if not is_bridge(G, current_node, neighbor):
                next_node = neighbor
                break

        if len(neighbors) == 0:
            break

        if next_node is None:
            next_node = neighbors[0]

        euler_path.append(str(current_node) + " -> " + str(next_node))
        G.remove_edge(current_node, next_node)
        current_node = next_node

    return euler_path

def largest_connected_component(G):
    visited = set()
    largest_component = set()
    for node in G.nodes():
        if node not in visited:
            component = set()
            dfs(node, G, component)
            if len(component) > len(largest_component):
                largest_component = component
            visited.update(component)

    largest_component_graph = G.subgraph(largest_component).copy()

    return largest_component_graph
 
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
        print("Generated graph:", graph)

        node_identifiers = list(range(0, V_size))
        nx_graph = create_graph_from_sequence(graph, node_identifiers)
        largest_component_graph = largest_connected_component(nx_graph)
        is_connected = (len(nx_graph.nodes) == len(largest_component_graph.nodes))
        while not is_connected:
            edge_switching(nx_graph, 1)
            largest_component_graph = largest_connected_component(nx_graph)
            is_connected = (len(nx_graph.nodes) == len(largest_component_graph.nodes))

        euler_cycle = find_euler_cycle(nx_graph.copy())
        print("Euler cycle:", euler_cycle)
        draw_graph_on_circle(nx_graph)

    else:
        print("Graph must have at least 3 vertices")
