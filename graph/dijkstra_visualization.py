# First, let's define a function to find the node with the smallest distance
# that has not been visited yet

# def min_distance(distances, visited):
#     # Initialize minimum distance for next node
#     min_val = float('inf')
#     min_index = -1

#     # Loop through all nodes to find minimum distance
#     for i in range(len(distances)):
#         if distances[i] < min_val and i not in visited:
#             min_val = distances[i]
#             min_index = i

#     return min_index

# # Now, let's implement Dijkstra's algorithm

# def dijkstra_algorithm(graph, start_node):

#     # Get total number of nodes in the graph
#     num_nodes = len(graph)

#     # Initialize distance and visited arrays
#     distances = [float('inf')] * num_nodes
#     visited = []

#     # Set distance at starting node to 0 and add to visited list 
#     distances[start_node] = 0

#     # Loop through all nodes to find shortest path to each node
#     for i in range(num_nodes):

#         # Find minimum distance node that has not been visited yet
#         current_node = min_distance(distances, visited)

#         # Add current_node to list of visited nodes
#         visited.append(current_node)

#         # Loop through all neighboring nodes of current_node 
#         for j in range(num_nodes):

#             # Check if there is an edge from current_node to neighbor
#             if graph[current_node][j] != 0:

#                 # Calculate the distance from start_node to neighbor, 
#                 # passing through current_node
#                 new_distance = distances[current_node] + graph[current_node][j]

#                 # Update the distance if it is less than previous recorded value 
#                 if new_distance < distances[j]:
#                     distances[j] = new_distance

#     # Return the list of the shortest distances to all nodes
#     return distances

# # Example graph represented as a 2D array
# graph = [[0, 7, 9, 0, 0, 14],
#          [7, 0, 10, 15, 0, 0],
#          [9, 10, 0, 11, 0, 2],
#          [0, 15, 11, 0, 6, 0],
#          [0, 0, 0, 6, 0 ,9],
#          [14. 0 ,2 ,0 ,9 ,8 ,10]]

# # Call Dijkstra's algorithm to find shortest paths from node 'A' (index of 'A' in the array is 0)
# shortest_distances = dijkstra_algorithm(graph, 'A')

# # Print the resulting shortest distances
# print(shortest_distances)

import networkx as nx
import matplotlib.pyplot as plt
import imageio
import os
import shutil
import heapq

def draw_graph(G, node_colors, edge_colors, pos, frame_id):
    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, node_color=node_colors, edge_color=edge_colors, with_labels=True, node_size=800, font_size=16)
    plt.savefig(f"frames/frame_{frame_id:03d}.png")
    plt.close()
    
def animate_dijkstra(graph, start_node):
    os.makedirs("frames", exist_ok=True)
    frame_id = 0
    
    pos = nx.spring_layout(graph, seed=42)
    visited = {node: False for node in graph.nodes}
    distances = {node: float("inf") for node in graph.nodes}
    distances[start_node] = 0
    pq = [(0, start_node)]

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        if visited[current_node]:
            continue

        visited[current_node] = True

        # Draw the graph at this step
        node_colors = ["green" if node == current_node else ("red" if visited[node] else "gray") for node in graph.nodes]
        edge_colors = ["black" for edge in graph.edges]
        draw_graph(graph, node_colors, edge_colors, pos, frame_id)
        frame_id += 1

        for neighbor, edge_weight in graph[current_node].items():
            new_distance = current_distance + edge_weight["weight"]

            if not visited[neighbor] and new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heapq.heappush(pq, (new_distance, neighbor))

    # Generate the animated GIF
    images = []
    for i in range(frame_id):
        images.append(imageio.imread(f"frames/frame_{i:03d}.png"))
    imageio.mimsave("dijkstra.gif", images, duration=1)

    # Clean up the frames folder
    shutil.rmtree("frames")

# Create a weighted graph
G = nx.Graph()
G.add_weighted_edges_from([(1, 2, 7), (1, 3, 9), (1, 6, 14), (2, 3, 10), (2, 4, 15),
                           (3, 4, 11), (3, 6, 2), (4, 5, 6), (5, 6, 9)])

# Run the animation for the graph
animate_dijkstra(G, 1)

# Display the resulting GIF (This will work in Jupyter Notebook)
from IPython.display import Image
Image(filename="dijkstra.gif")
