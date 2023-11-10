from itertools import permutations

def findDistance(graph, src):
    # Function to find the shortest distances from a source node to all other nodes using Bellman-Ford algorithm
    n = len(graph)
    distances = [float('inf')] * n  # Initialize distances with infinity
    distances[src] = 0  # Distance from source to itself is 0

    # Relax edges repeatedly to find the shortest distances
    for i in range(n):
        for u in range(n):
            for v in range(n):
                weight = graph[u][v]
                if distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight
    return distances

def bellmanford(graph):
    # Function to run Bellman-Ford algorithm for all nodes in the graph
    distance = []
    for vertex in range(len(graph)):
        distance.append(findDistance(graph, vertex))
    return distance

def negativeCycle(graph):
    # Function to check for the presence of a negative cycle in the graph
    distance = graph[0]
    n = len(graph)
    for u in range(n):
        for v in range(n):
            weight = graph[u][v]
            if distance[u] + weight < distance[v]:
                return True  # Negative cycle detected
    return False

def getPathTime(bunnies, graph):
    # Function to calculate the total time for a given bunny path in the graph
    time = 0
    time += graph[0][bunnies[0]]
    time += graph[bunnies[-1]][len(graph) - 1]
    for i in range(1, len(bunnies)):
        u = bunnies[i - 1]
        v = bunnies[i]
        time += graph[u][v]
    return time

def solution(times, times_limit):
    y_bunnies = len(times) - 2
    bunnies = [x for x in range(1, y_bunnies + 1)]
    distance = bellmanford(times)
    
    # Check for negative cycle in the graph
    if negativeCycle(distance):
        return list(range(y_bunnies))  # If negative cycle, return all bunnies

    # Try different combinations of bunnies to find a valid path within the time limit
    for i in range(y_bunnies, 0, -1):
        for perm in permutations(bunnies, i):
            time = getPathTime(perm, distance)
            if time <= times_limit:
                return [x - 1 for x in sorted(perm)]  # Convert to 0-based index
    return []  # If no valid path is found within the time limit
