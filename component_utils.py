def mark_connected_nodes(component_number, node_identifier, nx_graph, components):
    for neighbor_identifier in nx_graph.neighbors(node_identifier):
        if components[neighbor_identifier] == -1:
            components[neighbor_identifier] = component_number
            mark_connected_nodes(component_number, neighbor_identifier, nx_graph, components)


def components(nx_graph):
    nodes_list = list(nx_graph.nodes)
    number_of_nodes = len(nodes_list)

    component_number = 0
    components = dict(zip(nodes_list, [-1] * number_of_nodes))

    for node_identifier in components:
        if components[node_identifier] == -1:
            component_number += 1
            components[node_identifier] = component_number
            mark_connected_nodes(component_number, node_identifier, nx_graph, components)

    return components

def get_components_list(nx_graph, sort_by_length = True):
    components_list = {}

    graph_components = components(nx_graph)

    for node_identifier in graph_components:
        node_component = graph_components[node_identifier]
        if node_component not in components_list:
            components_list.update({node_component: []})
        components_list[node_component].append(node_identifier)

    if sort_by_length:
        components_list = dict(sorted(components_list.items(), key=lambda x: len(x[1]), reverse=True))

    return components_list
