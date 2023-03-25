from script_common import get_nx_graph_from_args

if __name__ == '__main__':
    nx_graph = get_nx_graph_from_args()
    adjacency_matrix = []

    nodes_list = list(nx_graph.nodes)
    number_of_nodes = len(nodes_list)
    for node_index in range(number_of_nodes):
        node = nodes_list[node_index]
        adjecency_matrix_row = []
        for tested_node_index in range(number_of_nodes):
            tested_node = nodes_list[tested_node_index]

            found_edge = False
            for edge in nx_graph.edges:
                if edge[0] == node and edge[1] == tested_node:
                    found_edge = True
                    break
                elif edge[0] == tested_node and edge[1] == node:
                    found_edge = True
                    break

            if found_edge:
                adjecency_matrix_row.append(1)
            else:
                adjecency_matrix_row.append(0)


        adjacency_matrix.append(adjecency_matrix_row)

    for adjecency_matrix_row in adjacency_matrix:
        print(" ".join([str(matrix_element) for matrix_element in adjecency_matrix_row]))
