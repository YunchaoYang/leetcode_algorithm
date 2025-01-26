# two kinds of implementation of Dijkstra algorithm

import heapq

def dijkstra(graph, start):
    # Initialize distances with infinity for all nodes
    distances = {node: float('inf') for node in graph}
    # Set the distance for the starting node as 0
    distances[start] = 0
    
    # Priority queue to store nodes to visit
    pq = [(0, start)]
    
    while pq:
        # Pop the node with the smallest distance from the priority queue
        current_distance, current_node = heapq.heappop(pq)
        
        # print("cur dist=", current_distance, "node=", current_node)
        # print(distances)
        
        # Check neighbors of the current node
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            # If a shorter path is found, update the distance
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                # Add the neighbor to the priority queue
                heapq.heappush(pq, (distance, neighbor))
    
    return distances

# Example graph
graph = {
    'A': {'B': 5, 'C': 3},
    'B': {'D': 2},
    'C': {'B': 1, 'D': 1},
    'D': {}
}

start_node = 'A'
result = dijkstra(graph, start_node)
print("Shortest distances from node", start_node, "to other nodes:", result)


def dijkstra_no_pq(graph, start):
    # Initialize distances with infinity for all nodes
    distances = {node: float('inf') for node in graph}
    # Set the distance for the starting node as 0
    distances[start] = 0
    
    unvisited = set(graph.keys())  # Set to keep track of unvisited nodes
    
    while unvisited:
        # Find the unvisited node with the minimum distance
        min_node = None
        for node in unvisited:
            if min_node is None or distances[node] < distances[min_node]:
                min_node = node
        
        unvisited.remove(min_node)  # Mark the node as visited
        
        # Update distances for neighbors of the current node
        for neighbor, weight in graph[min_node].items():
            distance = distances[min_node] + weight
            
            # If a shorter path is found, update the distance
            if distance < distances[neighbor]:
                distances[neighbor] = distance
    
    return distances

# Example graph
graph = {
    'A': {'B': 5, 'C': 3},
    'B': {'D': 2},
    'C': {'B': 1, 'D': 1},
    'D': {}
}

start_node = 'A'
result = dijkstra_no_pq(graph, start_node)
print("Shortest distances from node", start_node, "to other nodes:", result)
