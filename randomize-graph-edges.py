import argparse
import networkx as nx
import random
from script_common import draw_graph_on_circle

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('path_to_graph', help='path to graph in dot format')
    parser.add_argument('number_of_randomizations', type=int)
    args = parser.parse_args()
    graph_from_dot = nx.nx_pydot.read_dot(args.path_to_graph)
    nx_graph = nx.Graph(graph_from_dot)

    if len(nx_graph.nodes) < 4:
        print('za mało wierzchołków w grafie do zamiany krawędzi')
        exit()

    number_of_nodes = len(nx_graph.nodes)
    max_edges = number_of_nodes * (number_of_nodes - 1) / 2
    if len(nx_graph.edges) > max_edges - 2:
        print('za mało wolnych krawędzi do wykonywania zamian')
        exit()

    max_node_rank = number_of_nodes - 1
    #find four nodes with less thank maximum rank
    found_four_node_with_less_than_maximum_rank = False
    number_of_nodes_with_less_than_maximum_rank_found = 0
    for node in nx_graph.nodes:
        if nx_graph.degree(node) < max_node_rank:
            number_of_nodes_with_less_than_maximum_rank_found += 1
        if number_of_nodes_with_less_than_maximum_rank_found >= 4:
            found_four_node_with_less_than_maximum_rank = True
            break

    if not found_four_node_with_less_than_maximum_rank:
        print('stopnie wierzchołków grafu uniemożliwiają dokonywanie zamian')
        exit()


    original_edges = list(nx_graph.edges)
    edge_indexes = list(range(len(original_edges)))
    for i in range(args.number_of_randomizations):
        while True:
            edges_indexes_to_switch = random.sample(edge_indexes, 2)

            nodes_to_switch_edges = [
                original_edges[edges_indexes_to_switch[0]][0],
                original_edges[edges_indexes_to_switch[0]][1],
                original_edges[edges_indexes_to_switch[1]][0],
                original_edges[edges_indexes_to_switch[1]][1],
            ]
            all_nodes_unique = len(nodes_to_switch_edges) == len(set(nodes_to_switch_edges))
            if all_nodes_unique:
                #switch {{a, b}, {c, d}} to {{a, c}, {b, d}} or {{a, d}, {b, c}}
                node_a = original_edges[edges_indexes_to_switch[0]][0]
                node_b = original_edges[edges_indexes_to_switch[0]][1]
                node_c = original_edges[edges_indexes_to_switch[1]][0]
                node_d = original_edges[edges_indexes_to_switch[1]][1]

                if not nx_graph.has_edge(node_a, node_c) and not nx_graph.has_edge(node_b, node_d):
                    original_edges[edges_indexes_to_switch[0]] = (node_a, node_c)
                    original_edges[edges_indexes_to_switch[1]] = (node_b, node_d)
                    break
                elif not nx_graph.has_edge(node_a, node_d) and not nx_graph.has_edge(node_b, node_c):
                    original_edges[edges_indexes_to_switch[0]] = (node_a, node_d)
                    original_edges[edges_indexes_to_switch[1]] = (node_b, node_c)
                    break

    modified_graph = nx.Graph()
    modified_graph.add_nodes_from(nx_graph.nodes)
    modified_graph.add_edges_from(original_edges)
    draw_graph_on_circle(modified_graph)