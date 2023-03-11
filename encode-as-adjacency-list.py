import argparse
import networkx as nx

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('path_to_graph', help='path to graph in dot format')
    args = parser.parse_args()
    nx_graph = nx.Graph(nx.nx_pydot.read_dot(args.path_to_graph))
    adjacency_list = nx.generate_adjlist(nx_graph)
    for line in adjacency_list:
        print(line)