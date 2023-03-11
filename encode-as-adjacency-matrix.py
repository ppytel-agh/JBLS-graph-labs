from script_common import get_nx_graph_from_args
import networkx as nx

if __name__ == '__main__':
    nx_graph = get_nx_graph_from_args()
    adjacency_matrix = nx.adjacency_matrix(nx_graph)
    print(adjacency_matrix.todense())