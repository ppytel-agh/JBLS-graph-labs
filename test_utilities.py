def incidence_matrix_contains_edge(incidence_matrix, edge_nodes):
    number_of_edges = len(incidence_matrix[0])
    number_of_nodes = len(incidence_matrix)

    for edge_index in range(number_of_edges):
        nodes_found = 0
        for node_index in range(number_of_nodes):
            if incidence_matrix[node_index][edge_index] == 1:
                if node_index == edge_nodes[0] or node_index == edge_nodes[1]:
                    nodes_found += 1
                    if nodes_found == 2:
                        return True

    return False


def compare_incidence_matrices(template, compared):
    number_of_edges = len(template[0])
    number_of_nodes = len(template)

    if len(compared) != number_of_nodes:
        return ["number of nodes does not match"]

    if len(compared[0]) != number_of_edges:
        return ["number of degrees does not match"]

    differences = []
    for edge_index in range(number_of_edges):
        edge_nodes = []
        for node_index in range(number_of_nodes):
            if template[node_index][edge_index] == 1:
                edge_nodes.append(node_index)

        if not incidence_matrix_contains_edge(compared, edge_nodes):
            differences.append("edge ({}, {}) not found".format(edge_nodes[0], edge_nodes[1]))

    return differences


def compare_adjacency_lists(template, compared):
    template_keys = template.keys()
    number_of_nodes_in_template = len(template_keys)

    compared_keys = compared.keys()
    number_of_nodes_in_compared = len(compared_keys)

    if number_of_nodes_in_template != number_of_nodes_in_compared:
        return ["number_of_nodes_does_not_match"]

    differences = []
    for template_key in template_keys:
        found_key_in_compared = False
        for compared_key in compared_keys:
            if compared_key == template_key:
                found_key_in_compared = True
                number_of_adjacencies_in_template = len(template[template_key])
                number_of_adjacencies_in_compared = len(compared[compared_key])

                if number_of_adjacencies_in_template != number_of_adjacencies_in_compared:
                    differences.append("number of elements in {} key does not match".format(template_key))

                for template_element in template[template_key]:
                    found_element = False
                    for compared_element in compared[compared_key]:
                        if template_element == compared_element:
                            found_element = True
                            break

                    if not found_element:
                        differences.append("no adjacency {} in {} key".format(template_element, template_key))

        if not found_key_in_compared:
            differences.append("no key {} in compared".format(template_key))

    return differences


def assert_incidence_matrices_equal(template, compared):
    differences = compare_incidence_matrices(template, compared)
    if len(differences) > 0:
        raise AssertionError(differences[0])


def assert_adjacency_lists_equal(template, compared):
    differences = compare_adjacency_lists(template, compared)
    if len(differences) > 0:
        raise AssertionError(differences[0])
