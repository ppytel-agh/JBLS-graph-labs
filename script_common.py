import argparse
import networkx as nx
import matplotlib.pyplot as plt
def get_nx_graph_from_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('path_to_graph', help='path to graph in dot format')
    args = parser.parse_args()
    graph_from_dot = nx.nx_pydot.read_dot(args.path_to_graph)
    nx_graph = nx.Graph(graph_from_dot)
    return nx_graph

def draw_graph_on_circle(nx_graph):
    plt.gca().set_aspect('equal')
    plt.gca().add_patch(plt.Circle((0, 0), 1, fill=False, linestyle='--'))
    nx.draw_circular(nx_graph, with_labels=True)
    plt.show()