from script_common import get_nx_graph_from_args
import networkx as nx

if __name__ == '__main__':
    nx_graph = get_nx_graph_from_args()
    adjacency_list = nx.generate_adjlist(nx_graph)
    for line in adjacency_list:
        print(line)