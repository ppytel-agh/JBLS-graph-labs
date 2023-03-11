from script_common import get_nx_graph_from_args
import networkx as nx

if __name__ == '__main__':
    nx_graph = get_nx_graph_from_args()
    incidence_matrix = nx.incidence_matrix(nx_graph)
    print(incidence_matrix.todense())