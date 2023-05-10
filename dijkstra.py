# 3-2

import heapq
from create_graph_with_weights import create_graph_weights, plot_graph_weights

def dijkstra(G, start):
    shortest_paths = {v: (None, float('inf')) for v in G.nodes} # Dictionary: vertex -> (predecessor, distance)
    shortest_paths[start] = (None, 0) # Distance from the starting vertex to itself is 0
    unvisited_nodes = [(0, start)] # Priority queue: (distance, vertex)

    while unvisited_nodes:
        current_distance, current_node = heapq.heappop(unvisited_nodes)

        if shortest_paths[current_node][1] < current_distance:
            continue # Node has already been visited

        for neighbor, edge_weight in G[current_node].items():
            distance = current_distance + edge_weight["weight"]
            if distance < shortest_paths[neighbor][1]:
                shortest_paths[neighbor] = (current_node, distance)
                heapq.heappush(unvisited_nodes, (distance, neighbor))

    return shortest_paths

def print_shortest_paths(shortest_paths, start):
    print(f"START: s = {start}")
    for dest, (prev, dist) in shortest_paths.items():
        path = []
        current = dest
        while current != start:
            path.append(current)
            current = shortest_paths[current][0]
        path.append(start)
        path.reverse()
        print(f"d({dest}) = {dist}: [{' -> '.join(map(str, path))}]")

if __name__ == "__main__":
    # Use Dijkstra's algorithm on the generated graph
    start_node = 0
    G = create_graph_weights(5, 0.6)
    shortest_paths = dijkstra(G, start_node)

    # Print all shortest paths from the starting vertex
    print_shortest_paths(shortest_paths, start_node)
    plot_graph_weights(G)

