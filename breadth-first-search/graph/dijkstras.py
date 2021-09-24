from typing import List
from typing import Tuple
from typing import Dict
from typing import Optional
from queue import PriorityQueue
import math

class LazyDijkstras():
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
        """
        u: Node index
        v: point to
        w: Edge weight
        """
        self.graph[u].append((v, w))
    
    def run(self, start: int = 0) -> Tuple[Optional[int], Optional[int]]:
        dist: List[int] = [math.inf] * self.n
        dist[start] = 0
        
        self.pq.put((start, 0))
        
        while not self.pq.empty():
            index, _ = self.pq.get()
            self.visited[index] = True
            for edge in self.graph[index]:
                if self.visited[edge[0]]:
                    continue
                
                new_dist = dist[index] + edge[1]
                
                if new_dist < dist[edge[0]]:
                    dist[edge[0]] = new_dist
                    self.pq.put((edge[0], new_dist))
        return dist