from itertools import permutations

def findDistance(graph, src):
    n = len(graph)
    distances = [float('inf')] * n
    distances[src] = 0

    for i in range(n):
        for u in range(n):
            for v in range(n):
                weight = graph[u][v]
                if distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight
    return distances

def bellmanford(graph):
    distance = []
    for vertex in range(len(graph)):
        distance.append(findDistance(graph, vertex))
    return distance

def negativeCycle(graph):
    distance = graph[0]
    n = len(graph)
    for u in range(n):
        for v in range(n):
            weight = graph[u][v]
            if distance[u] + weight < distance[v]:
                return True
    return False

def getPathTime(bunnies, graph):
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
    if negativeCycle(distance):
        return list(range(y_bunnies))

    for i in range(y_bunnies, 0, -1):
        for perm in permutations(bunnies, i):
            time = getPathTime(perm, distance)
            if time <= times_limit:
                return [x - 1 for x in sorted(perm)]
    return []
