# 3-4

import numpy as np
import networkx as nx

from create_graph_with_weights import create_graph_weights, plot_graph_weights
from distance_matrix import all_pairs_distance_matrix

def graph_center(distance_matrix):
    row_sums = np.sum(distance_matrix, axis=1)
    center = np.argmin(row_sums)
    return center, row_sums[center]

def minimax_center(distance_matrix):
    row_max = np.max(distance_matrix, axis=1)
    minimax_center = np.argmin(row_max)
    return minimax_center, row_max[minimax_center]

if __name__ == "__main__":
    G = create_graph_weights(5, 0.6)
    distance_matrix = all_pairs_distance_matrix(G)
    # Calculate the graph center and minimax center
    center, center_value = graph_center(distance_matrix)
    minimax_center, minimax_center_value = minimax_center(distance_matrix)

    # Print the graph center and minimax center
    print(f"Graph center: {center} (sum of distances: {center_value})")
    print(f"Minimax center: {minimax_center} (max distance: {minimax_center_value})")
    plot_graph_weights(G)
