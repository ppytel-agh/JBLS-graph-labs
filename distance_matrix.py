# 3-3

import numpy as np
import networkx as nx

from dijkstra import dijkstra
from create_graph_with_weights import create_graph_weights, plot_graph_weights

def all_pairs_distance_matrix(G):
    n = len(G.nodes)
    distance_matrix = np.zeros((n, n), dtype=int)

    for i in range(n):
        shortest_paths = dijkstra(G, i)
        for j, (_, dist) in shortest_paths.items():
            distance_matrix[i, j] = dist

    return distance_matrix

if __name__ == "__main__":
    G = create_graph_weights(5, 0.6)

    # Calculate the distance matrix for the generated graph
    distance_matrix = all_pairs_distance_matrix(G)

    # Print the distance matrix
    print("Distance matrix:")
    print(distance_matrix)
    plot_graph_weights(G)