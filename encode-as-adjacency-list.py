from script_common import get_nx_graph_from_args

if __name__ == '__main__':
    nx_graph = get_nx_graph_from_args()

    adjacency_list = {}
    for node in nx_graph.nodes:
        node_neighbours_list = []
        for edge in nx_graph.edges:
            if(edge[0] == node):
                node_neighbours_list.append(edge[1])
            elif(edge[1] == node):
                node_neighbours_list.append(edge[0])

        adjacency_list.update({node: node_neighbours_list})

    for node in adjacency_list:
        node_neighbours_list = adjacency_list[node]
        print(str(node) + ": " + ", ".join([str(neighbour_node) for neighbour_node in node_neighbours_list]))