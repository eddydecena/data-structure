from typing import List

class KrushalAlgo():
    vertices: int
    graph: List[List[int]]
    
    def __init__(self, vertices: int) -> None:
        self.vertices = vertices
        self.graph = []
    
    def add_edge(self, u: int=0, v: int=0, w: int=0) -> None:
        self.graph.append((u, v, w))
    
    def find(self, parent: list, i: int) -> int:
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])
    
    def apply_union(self, parent, rank, x, y):
        xroot: int = self.find(parent, x)
        yroot: int = self.find(parent, y)
        
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else: 
            parent[yroot] = xroot
            rank[xroot] += 1
    
    def kruskal_algo(self) -> None:
        result: list = []
        i: int = 0 
        e: int = 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent: list = []
        rank: list = []
        for node in range(self.vertices):
            parent.append(node)
            rank.append(0)
        while e < self.vertices - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.apply_union(parent, rank, x, y)
        for u, v, weight in result:
            print("%d - %d: %d" % (u, v, weight))