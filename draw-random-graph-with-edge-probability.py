import argparse
import networkx as nx
from script_common import draw_graph_on_circle
import random

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('n', type=int, help='number of vertices')
    parser.add_argument('p', type=float, help='probability of each edge')
    args = parser.parse_args()

    vertices = list(range(1, args.n+1))
    edges = []
    for vertex in vertices:
        for other_vertex in range(vertex+1, args.n+1):
            if random.uniform(0, 1) <= args.p:
                edge = (vertex, other_vertex)
                edges.append(edge)

    nx_graph = nx.Graph()
    nx_graph.add_nodes_from(vertices)
    nx_graph.add_edges_from(edges)

    draw_graph_on_circle(nx_graph)
