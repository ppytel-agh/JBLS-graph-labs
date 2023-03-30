import argparse
import networkx as nx
import random
from script_common import draw_graph_on_circle

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('path_to_graph', help='path to graph in dot format')
    parser.add_argument('number_of_randomizations', type=int)
    args = parser.parse_args()
    graph_from_dot = nx.nx_pydot.read_dot(args.path_to_graph)
    nx_graph = nx.Graph(graph_from_dot)

    original_edges = list(nx_graph.edges)
    edge_indexes = list(range(len(original_edges)))
    for i in range(args.number_of_randomizations):
        while True:
            edges_indexes_to_switch = random.sample(edge_indexes, 2)

            nodes_to_switch_edges = [
                original_edges[edges_indexes_to_switch[0]][0],
                original_edges[edges_indexes_to_switch[0]][1],
                original_edges[edges_indexes_to_switch[1]][0],
                original_edges[edges_indexes_to_switch[1]][1],
            ]
            all_nodes_unique = len(nodes_to_switch_edges) == len(set(nodes_to_switch_edges))
            if all_nodes_unique:
                new_edge1 = (original_edges[edges_indexes_to_switch[0]][0], original_edges[edges_indexes_to_switch[1]][1])
                new_edge2 = (original_edges[edges_indexes_to_switch[0]][1], original_edges[edges_indexes_to_switch[1]][0])
                original_edges[edges_indexes_to_switch[0]] = new_edge1
                original_edges[edges_indexes_to_switch[1]] = new_edge2
                break

    modified_graph = nx.Graph()
    modified_graph.add_nodes_from(nx_graph.nodes)
    modified_graph.add_edges_from(original_edges)
    draw_graph_on_circle(modified_graph)