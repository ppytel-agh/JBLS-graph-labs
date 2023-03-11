from script_common import get_nx_graph_from_args
from script_common import draw_graph_on_circle
import networkx as nx

if __name__ == '__main__':
    nx_graph = get_nx_graph_from_args()
    draw_graph_on_circle(nx_graph)