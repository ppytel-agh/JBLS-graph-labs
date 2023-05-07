# 3-5

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

from create_graph_with_weights import create_graph_weights, plot_graph_weights

import heapq

def prim(G):
    n = len(G.nodes)
    visited = [False] * n
    min_spanning_tree = []

    # Start from the first vertex
    start_vertex = 0
    visited[start_vertex] = True

    # Create a priority queue of edges
    edges = []
    for _, adj in G.adj[start_vertex].items():
        heapq.heappush(edges, (adj['weight'], start_vertex, _))

    while edges:
        w, u, v = heapq.heappop(edges)

        if not visited[v]:
            min_spanning_tree.append((u, v, w))
            visited[v] = True

            # Add new edges to the priority queue
            for next_vertex, next_weight in G.adj[v].items():
                if not visited[next_vertex]:
                    heapq.heappush(edges, (next_weight['weight'], v, next_vertex))

    return min_spanning_tree

if __name__ == "__main__":
    # Calculate the minimum spanning tree using Kruskal's algorithm
    G = create_graph_weights(8, 0.5)

    min_spanning_tree = prim(G)

    # Create a new graph for the minimum spanning tree
    min_spanning_tree_graph = nx.Graph()

    # Add vertices to the new graph
    min_spanning_tree_graph.add_nodes_from(G.nodes)

    # Add edges from the minimum spanning tree to the new graph
    min_spanning_tree_graph.add_weighted_edges_from(min_spanning_tree)

    # Create a figure
    fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(15, 6))

    # Draw the original graph
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, font_weight='bold', node_color='blue', node_size=700, ax=ax[0])
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, ax=ax[0])
    ax[0].set_title("Original Graph")

    # Draw the minimum spanning tree graph with the same positions as the original graph
    nx.draw(min_spanning_tree_graph, pos, with_labels=True, font_weight='bold', node_color='orange', node_size=700, ax=ax[1])
    edge_labels_mst = nx.get_edge_attributes(min_spanning_tree_graph, 'weight')
    nx.draw_networkx_edge_labels(min_spanning_tree_graph, pos, edge_labels=edge_labels_mst, ax=ax[1])
    ax[1].set_title("Minimum Spanning Tree")

    # Display the plots
    plt.show()



