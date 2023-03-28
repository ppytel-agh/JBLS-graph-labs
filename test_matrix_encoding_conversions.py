from unittest import TestCase
from test_utilities import assert_incidence_matrices_equal
from test_utilities import assert_adjacency_lists_equal

from matrix_encoding_conversions import convert_adjacency_matrix_to_incidence_matrix
from matrix_encoding_conversions import convert_adjacency_matrix_to_adjacency_list
from matrix_encoding_conversions import convert_incidence_matrix_to_adjacency_matrix
from matrix_encoding_conversions import convert_incidence_matrix_to_adjacency_list
from matrix_encoding_conversions import convert_adjacency_list_to_adjacency_matrix
from matrix_encoding_conversions import convert_adjacency_list_to_incidence_matrix

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
    node_identifiers = list(range(1, 13))

    def test_convert_adjacency_matrix_to_incidence_matrix(self):
        actual_incidence_matrix = convert_adjacency_matrix_to_incidence_matrix(Test.adjacency_matrix)
        assert_incidence_matrices_equal(
            Test.incidence_matrix,
            actual_incidence_matrix
        )

    def test_convert_adjacency_matrix_to_adjacency_list(self):
        actual_adjacency_list = convert_adjacency_matrix_to_adjacency_list(Test.adjacency_matrix, Test.node_identifiers)
        assert_adjacency_lists_equal(Test.adjacency_list, actual_adjacency_list)

    def test_convert_incidence_matrix_to_adjacency_matrix(self):
        actual_adjacencya_matrix = convert_incidence_matrix_to_adjacency_matrix(Test.incidence_matrix)
        self.assertEqual(Test.adjacency_matrix, actual_adjacencya_matrix)

    def test_convert_incidence_matrix_to_adjacency_list(self):
        actual_adjacency_list = convert_incidence_matrix_to_adjacency_list(Test.incidence_matrix, Test.node_identifiers)
        assert_adjacency_lists_equal(Test.adjacency_list, actual_adjacency_list)

    def test_convert_adjacency_list_to_adjacency_matrix(self):
        actual_adjacency_matrix = convert_adjacency_list_to_adjacency_matrix(Test.adjacency_list)
        self.assertEqual(Test.adjacency_matrix, actual_adjacency_matrix)

    def test_convert_adjacency_list_to_incidence_matrix(self):
        actual_incidence_matrix = convert_adjacency_list_to_incidence_matrix(Test.adjacency_list)
        assert_incidence_matrices_equal(Test.incidence_matrix, actual_incidence_matrix)