from script_common import get_nx_graph_from_args
import networkx as nx

if __name__ == '__main__':
    nx_graph = get_nx_graph_from_args()

    nodes_list = list(nx_graph.nodes)
    number_of_nodes = len(nodes_list)

    edges_list = list(nx_graph.edges)
    number_of_edges = len(edges_list)

    incidence_matrix = []
    for node_index in range(number_of_nodes):
        node = nodes_list[node_index]
        incidence_matrix_row = []
        for tested_edge_index in range(number_of_edges):
            tested_edge = edges_list[tested_edge_index]
            if tested_edge[0] == node or tested_edge[1] == node:
                incidence_matrix_row.append(1)
            else:
                incidence_matrix_row.append(0)

        incidence_matrix.append(incidence_matrix_row)

    for incidence_matrix_row in incidence_matrix:
        print(" ".join([str(matrix_element) for matrix_element in incidence_matrix_row]))
