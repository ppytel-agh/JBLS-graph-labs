# 2-5

import argparse
import networkx as nx
import random

from script_common import draw_graph_on_circle

def is_k_regular(G, k):
    if not G:
        return False
    
    degrees = [G.degree(node) for node in G.nodes()]
    first_degree = k

    for degree in degrees[1:]:
        if degree != first_degree:
            return False

    return True

def random_k_regular_graph(n, k):
    if n * k % 2 != 0:
        raise ValueError("n * k must be even number")
    elif k >= n:
        raise ValueError("n must be greater than k")
    elif k <= 0 or n <= 0:
        raise ValueError("n and k must be positive values")
    
    degree_seq = [k] * n

    while True:
        stubs = [node for node, degree in enumerate(degree_seq) for _ in range(degree)]
        random.shuffle(stubs)

        edges = set()
        while len(stubs) >= 2:
            edge = tuple(sorted((stubs.pop(), stubs.pop())))
            if edge[0] != edge[1]:
                edges.add(edge)

        G = nx.Graph(edges)

        if is_k_regular(G, k):
            break

    return G

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('n_k', type=int, nargs=2)
    args = parser.parse_args()
    n = args.n_k[0]
    k = args.n_k[1]

    G = random_k_regular_graph(n, k)

    draw_graph_on_circle(G)
