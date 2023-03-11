import argparse
import networkx as nx
def get_nx_graph_from_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('path_to_graph', help='path to graph in dot format')
    args = parser.parse_args()
    nx_graph = nx.Graph(nx.nx_pydot.read_dot(args.path_to_graph))
    return nx_graph