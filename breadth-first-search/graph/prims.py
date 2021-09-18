from typing import List
from typing import Tuple
from typing import Dict
from typing import Optional
from queue import PriorityQueue

class LazyPrims():
    graph: Dict[int, List[Tuple[int]]]
    n: int
    m: int
    visited: List[bool]
    edgeCount: int
    mstCost: int
    mstEdges: int
    pq: PriorityQueue
    
    def __init__(self, vertices: int) -> None:
        self.n = vertices
        self.m = self.n - 1
        self.visited = [False] * self.n
        self.edgeCount = 0
        self.mstCost = 0
        self.mstEdges = [None] * self.m
        self.pq = PriorityQueue()
        self.graph = {}
        
        for i in range(vertices):
            self.graph[i] = []
    
    def add_edge(self, u: int=0, v: int=0, w: int=0) -> None:
        self.graph[u].append((v, w))
    
    def enqueue_edges(self, node_index: int) -> None:
        self.visited[node_index] = True
        
        edges = self.graph[node_index]
        for edge in edges:
            if not self.visited[edge[0]]:
                self.pq.put(edge)
    
    def run(self, start: int = 0) -> Tuple[Optional[int], Optional[int]]:
        self.enqueue_edges(start)
        
        while (not self.pq.empty() and self.edgeCount != self.m):
            edge = self.pq.get()
            
            if self.visited[edge[0]]:
                continue
            
            self.mstEdges[self.edgeCount] = edge
            self.edgeCount += 1
            self.mstCost += edge[1]
            
            self.enqueue_edges(edge[0])
        
        if (self.edgeCount != self.m):
            return None, None
        
        return (self.mstCost, self.mstEdges)