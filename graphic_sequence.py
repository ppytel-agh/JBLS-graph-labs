import networkx as nx


def is_sequence_graphic(sequence_to_check):
    sequence_copy = sequence_to_check[:]
    sequence_copy.sort(reverse=True)
    if sequence_copy[-1] < 0:
        # invalid sequence, node degree cannot be lower than 0
        return False

    number_of_nodes = len(sequence_copy)
    if sequence_copy[0] >= number_of_nodes:
        # to few nodes to edges for biggest degree
        return False

    degrees_sum = sum(sequence_copy)
    if degrees_sum == 0:
        # graph with no edges
        return True

    while True:
        biggest_degree = sequence_copy[0]
        # construct edges from biggest degree node to other nodes with slightly lower degree
        sequence_copy[0] = 0
        for i in range(1, biggest_degree+1):
            sequence_copy[i] = sequence_copy[i] - 1

        # check if any new degree is lower than 0
        for degree_index in range(number_of_nodes):
            if sequence_copy[degree_index] < 0:
                return False

        degrees_sum = sum(sequence_copy)
        if degrees_sum == 0:
            # all edges distributed
            return True

        sequence_copy.sort(reverse=True)


def create_graph_from_sequence(graphic_sequence, node_identifiers):
    if not is_sequence_graphic(graphic_sequence):
        raise ValueError("Invalid graphic sequence!")

    nx_graph = nx.Graph()
    nx_graph.add_nodes_from(node_identifiers)

    sequence_dict = dict(zip(node_identifiers, graphic_sequence))
    sorted_dict = dict(sorted(sequence_dict.items(), key=lambda x: x[1], reverse=True))

    while sum(sorted_dict.values()) > 0:
        keys = list(sorted_dict.keys())
        node_identifier = keys[0]
        biggest_degree = sorted_dict[node_identifier]
        for adjacent_node_key_index in range(1, biggest_degree + 1):
            adjacent_node_identifier = keys[adjacent_node_key_index]
            nx_graph.add_edge(node_identifier, adjacent_node_identifier)
            sorted_dict[adjacent_node_identifier] -= 1

        sorted_dict[node_identifier] = 0
        sorted_dict = dict(sorted(sorted_dict.items(), key=lambda x: x[1], reverse=True))

    return nx_graph

