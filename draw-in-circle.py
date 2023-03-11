from script_common import get_nx_graph_from_args
import networkx as nx
import matplotlib.pyplot as plt

if __name__ == '__main__':
    nx_graph = get_nx_graph_from_args()
    nx.draw_circular(nx_graph)
    plt.show()