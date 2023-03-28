import argparse
import networkx as nx
from script_common import draw_graph_on_circle
import random

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('n', type=int, help='number of vertices')
    parser.add_argument('l', type=int, help='number of edges')
    args = parser.parse_args()

    vertices = list(range(1, args.n+1))
    edges = []
    for edge_index in range(args.l):
        found_same_edge = True
        while found_same_edge:
            starting_edge_identifier = random.randint(1, args.n)
            end_edge_identifier = starting_edge_identifier
            while end_edge_identifier == starting_edge_identifier:
                end_edge_identifier = random.randint(1, args.n)

            found_same_edge = False
            for existing_edge in edges:
                if (existing_edge[0] == starting_edge_identifier and existing_edge[1] == end_edge_identifier) \
                        or (existing_edge[1] == starting_edge_identifier and existing_edge[0] == end_edge_identifier):
                    found_same_edge = True
                    break

        new_edge = (starting_edge_identifier, end_edge_identifier)
        edges.append(new_edge)

    nx_graph = nx.Graph()
    nx_graph.add_nodes_from(vertices)
    nx_graph.add_edges_from(edges)

    draw_graph_on_circle(nx_graph)
