import heapq

def dijkstra(graph, start):
    vertices = set(graph.keys())
    
    distances = {vertex: float('inf') for vertex in vertices}
    distances[start] = 0
    
    queue = [(0, start)]
    
    while queue:
        current_distance, current_vertex = heapq.heappop(queue)
        
        if current_distance > distances[current_vertex]:
            continue
            
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
    
    return distances

graph = {
    'A': {'B': 5, 'D': 9, 'E': 2},
    'B': {'A': 5, 'C': 2},
    'C': {'B': 2, 'D': 3},
    'D': {'A': 9, 'C': 3, 'E': 2},
    'E': {'A': 2, 'D': 2}
}

start_vertex = 'A'
distances = dijkstra(graph, start_vertex)
print(distances)
