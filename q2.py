import heapq
ipair=tuple

class graph:
    def __init__(self,v:int):
        self.v=v
        self.adj=[[] for _ in range(v)]
    def addedge(self,u:int,v:int,w:int):
        self.adj[u].append((v,w))
        self.adj[v].append((u,w))

    def shortest(self,src:int):
        pq=[]
        dist=[float('inf')]*self.v
        dist[src]=0
        while pq:
            d,u=heapq.heappop(pq)
            for v,weight in self.adj[u]:
                if dist[v]>dist[u]+weight:
                    dist[v]=dist[u]+weight
                    heapq.heappush(pq,(dist[v],v))
        for i in range(self.v):
            print(f"{i}\t\t {dist[i]}")

v=9
g=graph(v)
g.addedge(0,1,4)
g.addedge(0,7,8)
g.addedge(1,2,8)
g.addedge(1,7,11)
g.addedge(2,3,7)
g.addedge(2,8,2)

g.shortest(0)