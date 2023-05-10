ZESTAWY

zestaw 1

z1 - encode-as-adjacency-matrix.py, encode-as-incidence-matrix.py, encode-as-adjacency-list.py, matrix_encoding_conversions.py
z2 - draw-in-circle.py
z3 - draw-random-graph-with-number-of-edges.py, draw-random-graph-with-edge-probability.py

zestaw 2

z1
check-if-sequence-is-graphic-and-construct-graph-if-is.py <ranks+> [output dot file name]

$python3 check-if-sequence-is-graphic-and-construct-graph-if-is.py 4 2 2 3 2 1 4 2 2 2 2 --output_name graph_for_randomization
valid sequence, generates graph and writes it out

$python3 check-if-sequence-is-graphic-and-construct-graph-if-is.py 4 4 3 1 2
invalid sequence

z2
randomize-graph-edges.py <path to dot file> <number of swaps>

$python3 randomize-graph-edges.py ./graph_for_randomization.dot 10
swaps 10 edges, persists vertice ranks

z3
find-giant-component.py <path to dot file>

$pyhon3 find-giant-component.py ./graph_for_randomization.dot

MODUŁY

script_common.py - funkcje do obsługi obiektów nxgraph
test_matrix_encoding_conversions.py - moduł testujący funkcje do konwersji
test_utilities.py - funkcje do porównywania macierzy incidencji i list sąsiedztwa
