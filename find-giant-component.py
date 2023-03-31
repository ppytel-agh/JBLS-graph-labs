from script_common import get_nx_graph_from_args
from component_utils import get_components_list

if __name__ == '__main__':
    nx_graph = get_nx_graph_from_args()
    components_list = get_components_list(nx_graph)
    for component_id in components_list:
        print("{}: {}".format(component_id, components_list[component_id]))
