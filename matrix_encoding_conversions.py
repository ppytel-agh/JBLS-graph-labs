def convert_adjacency_matrix_to_incidence_matrix(adjacency_matrix):
    number_of_nodes = len(adjacency_matrix)
    edges_list = []
    for node_index in range(number_of_nodes):
        # skip the same index and already checked edges
        for possible_adjacent_node_index in range(node_index+1, number_of_nodes):
            if adjacency_matrix[node_index][possible_adjacent_node_index] == 1:
                edge = (node_index, possible_adjacent_node_index)
                edges_list.append(edge)

    incidence_matrix = []
    for node_index in range(number_of_nodes):
        incidence_matrix_row = []
        for edge in edges_list:
            if edge[0] == node_index or edge[1] == node_index:
                incidence_matrix_row.append(1)
            else:
                incidence_matrix_row.append(0)

        incidence_matrix.append(incidence_matrix_row)

    return incidence_matrix


def convert_adjacency_matrix_to_adjacency_list(adjacency_matrix, node_identifiers):
    number_of_nodes = len(adjacency_matrix)
    adjacency_list = {}
    for node_index in range(number_of_nodes):
        node_identifier = node_identifiers[node_index]
        node_neighbors = []
        # skip the same index and already checked edges
        for possible_adjacent_node_index in range(number_of_nodes):
            if adjacency_matrix[node_index][possible_adjacent_node_index] == 1:
                adjacent_node_identifier = node_identifiers[possible_adjacent_node_index]
                node_neighbors.append(adjacent_node_identifier)

        adjacency_list.update({node_identifier: node_neighbors})

    return adjacency_list


def convert_incidence_matrix_to_adjacency_matrix(incidence_matrix):
    number_of_nodes = len(incidence_matrix)
    number_of_edges = len(incidence_matrix[0])

    adjacency_matrix = []
    for node_index in range(number_of_nodes):
        adjacency_matrix_row = []
        for possible_adjacent_node_index in range(number_of_nodes):
            if node_index == possible_adjacent_node_index:
                # node cannot be adjacent to itself
                adjacency_matrix_row.append(0)
            else:
                found_edge = False
                for edge_index in range(number_of_edges):
                    if incidence_matrix[node_index][edge_index] == 1 \
                            and incidence_matrix[possible_adjacent_node_index][edge_index] == 1:
                        found_edge = True
                        break

                if found_edge:
                    adjacency_matrix_row.append(1)
                else:
                    adjacency_matrix_row.append(0)

        adjacency_matrix.append(adjacency_matrix_row)

    return adjacency_matrix

def convert_incidence_matrix_to_adjacency_list(incidence_matrix, node_identifiers):
    number_of_nodes = len(incidence_matrix)
    number_of_edges = len(incidence_matrix[0])

    adjacency_list = {}
    for node_index in range(number_of_nodes):
        node_identifier = node_identifiers[node_index]
        node_neighbors = []
        for edge_index in range(number_of_edges):
            if incidence_matrix[node_index][edge_index] == 1:
                for possible_adjacent_node_index in range(number_of_nodes):
                    if possible_adjacent_node_index == node_index:
                        continue
                    if incidence_matrix[possible_adjacent_node_index][edge_index] == 1:
                        adjacent_node_identifier = node_identifiers[possible_adjacent_node_index]
                        node_neighbors.append(adjacent_node_identifier)
                        break

        adjacency_list.update({node_identifier: node_neighbors})

    return adjacency_list


def convert_adjacency_list_to_adjacency_matrix(adjacency_list):
    adjacency_matrix = []

    node_identifiers = list(adjacency_list)
    number_of_nodes = len(node_identifiers)

    node_indexes = {}
    for node_index in range(number_of_nodes):
        node_identifier = node_identifiers[node_index]
        node_indexes.update({node_identifier: node_index})

    for row_node_index in range(number_of_nodes):
        node_identifier = node_identifiers[row_node_index]
        adjacency_matrix_row = []
        neighbor_identifiers = adjacency_list[node_identifier]
        for column_node_index in range(number_of_nodes):
            found_neighbor = False
            for neighbor_identifier in neighbor_identifiers:
                neighbor_index = node_indexes[neighbor_identifier]
                if neighbor_index == column_node_index:
                    found_neighbor = True
                    break
            if found_neighbor:
                adjacency_matrix_row.append(1)
            else:
                adjacency_matrix_row.append(0)

        adjacency_matrix.append(adjacency_matrix_row)

    return adjacency_matrix


def convert_adjacency_list_to_incidence_matrix(adjacency_list):
    incidence_matrix = []

    node_identifiers = list(adjacency_list)
    number_of_nodes = len(node_identifiers)

    node_indexes = {}
    for node_index in range(number_of_nodes):
        node_identifier = node_identifiers[node_index]
        node_indexes.update({node_identifier: node_index})

    edges_with_indexes = []
    for node_index in range(number_of_nodes):
        node_identifier = node_identifiers[node_index]
        neighbour_identifiers = adjacency_list[node_identifier]
        for neighbour_identifier in neighbour_identifiers:
            neighbour_index = node_indexes[neighbour_identifier]
            # prevent doubling edges
            if neighbour_index > node_index:
                edge = (node_index, neighbour_index)
                edges_with_indexes.append(edge)

    number_of_edges = len(edges_with_indexes)
    for row_node_index in range(number_of_nodes):
        incidence_matrix_row = []
        for column_edge_index in range(number_of_edges):
            if edges_with_indexes[column_edge_index][0] == row_node_index:
                incidence_matrix_row.append(1)
            elif edges_with_indexes[column_edge_index][1] == row_node_index:
                incidence_matrix_row.append(1)
            else:
                incidence_matrix_row.append(0)

        incidence_matrix.append(incidence_matrix_row)

    return incidence_matrix
