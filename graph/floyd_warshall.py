def floyd_warshall(graph):
    """
    Floyd-Warshall algorithm to find the shortest paths 
    between all pairs of vertices.

    :param graph: 2D list representing the adjacency matrix of the graph.
                  graph[i][j] is the weight of the edge from i to j, or inf 
                  if no edge exists.
    :return: 2D list of shortest distances between all pairs of vertices.
    """
    # Number of vertices
    V = len(graph)
    
    # Initialize the distance matrix
    dist = [row[:] for row in graph]  # Copy the input graph

    # Main DP loop: Add intermediate vertices one by one
    for k in range(V):
        for i in range(V):
            for j in range(V):
                # Update the shortest distance from i to j via vertex k
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    # O(V^3)
    
    # Check for negative weight cycles
    for i in range(V):
        if dist[i][i] < 0:
            print("Graph contains a negative weight cycle.")
            return None

    return dist



# Input graph as an adjacency matrix
INF = float('inf')
graph = [
    [0, 3, INF, 5],
    [2, 0, INF, 4],
    [INF, 1, 0, INF],
    [INF, INF, 2, 0]
]

# Run Floyd-Warshall
shortest_paths = floyd_warshall(graph)

if shortest_paths:
    print("Shortest distances between all pairs of vertices:")
    for row in shortest_paths:
        print(row)
