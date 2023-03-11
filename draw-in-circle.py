from script_common import get_nx_graph_from_args
import networkx as nx
import matplotlib.pyplot as plt

if __name__ == '__main__':
    nx_graph = get_nx_graph_from_args()
    plt.gca().set_aspect('equal')
    plt.gca().add_patch(plt.Circle((0, 0), 1, fill=False, linestyle='--'))
    nx.draw_circular(nx_graph, with_labels = True)
    plt.show()