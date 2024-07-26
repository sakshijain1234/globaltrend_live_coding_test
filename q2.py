import heapq

def dijkstra(graph, source):
    # Initialize distances with infinity and set the distance to the source as 0
    distances = {vertex: float('inf') for vertex in graph}
    distances[source] = 0

    # Create a priority queue to store vertices with their current distance
    priority_queue = [(0, source)]
    
    while priority_queue:
        # Pop the vertex with the smallest distance
        current_distance, current_vertex = heapq.heappop(priority_queue)
        
        # If the popped distance is greater than the recorded distance, continue
        if current_distance > distances[current_vertex]:
            continue
        
        # Update the distances to the adjacent vertices
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            
            # If a shorter path is found, update the distance and push to the queue
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

# Sample test case
graph = {0: {1: 4, 2: 1}, 1: {3: 1}, 2: {1: 2, 3:5},3:{}}
source=0
print(dijkstra(graph, source))


# import heapq
# ipair=tuple

# class graph:
#     def __init__(self,v:int):
#         self.v=v
#         self.adj=[[] for _ in range(v)]
#     def addedge(self,u:int,v:int,w:int):
#         self.adj[u].append((v,w))
#         self.adj[v].append((u,w))

#     def shortest(self,src:int):
#         pq=[]
#         dist=[float('inf')]*self.v
#         dist[src]=0
#         while pq:
#             d,u=heapq.heappop(pq)
#             for v,weight in self.adj[u]:
#                 if dist[v]>dist[u]+weight:
#                     dist[v]=dist[u]+weight
#                     heapq.heappush(pq,(dist[v],v))
#         for i in range(self.v):
#             print(f"{i}\t\t {dist[i]}")

# v=9
# g=graph(v)
# g.addedge(0,1,4)
# g.addedge(0,7,8)
# g.addedge(1,2,8)
# g.addedge(1,7,11)
# g.addedge(2,3,7)
# g.addedge(2,8,2)

# g.shortest(0)