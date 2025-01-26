import heapq

def prim(graph):
    minimum_spanning_tree = []
    vertices = set(graph.keys())
    start_vertex = vertices.pop()  # Start from an arbitrary vertex

    visited = {start_vertex}

    edges = [
        (cost, start_vertex, neighbor) for neighbor, cost in graph[start_vertex]
    ]
    
    heapq.heapify(edges) #

    while edges:
        cost, current_vertex, next_vertex = heapq.heappop(edges)

        if next_vertex not in visited:
            visited.add(next_vertex)
            minimum_spanning_tree.append((current_vertex, next_vertex, cost))

            for neighbor, edge_cost in graph[next_vertex]:
                if neighbor not in visited:
                    heapq.heappush(edges, (edge_cost, next_vertex, neighbor))

    return minimum_spanning_tree


# Example usage:
example_graph = {
    'A': [('B', 7), ('D', 5)],
    'B': [('A', 7), ('C', 8), ('D', 9), ('E', 7)],
    'C': [('B', 8), ('E', 5)],
    'D': [('A', 5), ('B', 9), ('E', 15), ('F', 6)],
    'E': [('B', 7), ('C', 5), ('D', 15), ('F', 8)],
    'F': [('D', 6), ('E', 8)]
}

minimum_spanning_tree = prim(example_graph)
print("Minimum Spanning Tree:")
for edge in minimum_spanning_tree:
    print(edge)
