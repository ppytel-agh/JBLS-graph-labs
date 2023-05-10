import argparse
import os
from networkx.drawing.nx_pydot import write_dot

from graphic_sequence import is_sequence_graphic
from graphic_sequence import create_graph_from_sequence
from script_common import draw_graph_on_circle

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('potential_sequence', type=int, nargs="+", help='sequence_to_check')
    parser.add_argument('--output_name', type=str, help='name of dot file to output generated graph')
    args = parser.parse_args()

    if is_sequence_graphic(args.potential_sequence):
        number_of_nodes = len(args.potential_sequence)
        node_identifiers = list(range(1, number_of_nodes + 1))
        nx_graph = create_graph_from_sequence(args.potential_sequence, node_identifiers)

        if args.output_name:
            filename = f'{args.output_name}.dot'
            output_path = os.path.join(os.getcwd(), filename)

            write_dot(nx_graph, output_path)

        draw_graph_on_circle(nx_graph)
    else:
        print("sequence is not graphic")