from unittest import TestCase

from matrix_encoding_conversions import convert_adjacency_matrix_to_incidence_matrix
class Test(TestCase):
    adjacency_matrix = [
        [0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
        [1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0],
        [1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0],
        [1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1],
        [0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0]
    ]
    incidence_matrix = [
      [1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
      [0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
      [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
      [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1]
    ]
    adjacency_list = {
        1: [2, 5, 6],
        2: [1, 3, 6],
        3: [2, 4, 5, 12],
        4: [3, 8, 9, 11],
        5: [1, 3, 7, 9],
        6: [1, 2, 7],
        7: [5, 6, 8],
        8: [4, 7, 9, 12],
        9: [4, 5, 8, 10],
        10: [9],
        11: [4],
        12: [3, 8],
    }

    def incidence_matrix_contains_edge(incidence_matrix, edge_nodes):
        number_of_edges = len(incidence_matrix[0])
        number_of_nodes = len(incidence_matrix)

        for edge_index in range(number_of_edges):
            nodes_found = 0
            for node_index in range(number_of_nodes):
                if node_index == edge_nodes[0] or node_index == edge_nodes[1]:
                    nodes_found += 1
                    if nodes_found == 2:
                        return True

        return False
    def assertIncidenceMatricesEqual(self, expected, actual):
        number_of_edges = len(expected[0])
        number_of_nodes = len(expected)

        if len(actual) != number_of_nodes:
            raise AssertionError("number of nodes does not match")
            return

        if len(actual[0]) != number_of_edges:
            raise AssertionError("number of deges does not match")
            return

        for edge_index in range(number_of_edges):
            edge_nodes = []
            for node_index in range(number_of_nodes):
                if expected[node_index][edge_index] == 1:
                    edge_nodes.append(node_index)

            if not Test.incidence_matrix_contains_edge(actual, edge_nodes):
                raise AssertionError("edge " + edge_index + " not found")


    def test_convert_adjacency_matrix_to_incidence_matrix(self):
        actual_incidence_matrix = convert_adjacency_matrix_to_incidence_matrix(Test.adjacency_matrix)
        self.assertIncidenceMatricesEqual(
            Test.incidence_matrix,
            actual_incidence_matrix
        )
