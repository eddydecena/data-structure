from typing import List
from typing import Tuple
from typing import Dict
from typing import Optional
from queue import PriorityQueue
import heapq
import math

class BellmanFord():
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
        self.ipq = []
        self.graph = {}
        
        heapq.heapify(self.ipq)
        
        for i in range(vertices):
            self.graph[i] = []
    
    def add_edge(self, u: int=0, v: int=0, w: int=0) -> None:
        """
        u: Actual node
        v: Edge to
        w: Edge weight
        """
        self.graph[u].append((v, w))
    
    def run(self, start: int = 0) -> Tuple[List[int], List[int]]:
        dist: List[int] = [math.inf] * self.n
        pred: List[int] = [None] * self.n
        
        dist[start] = 0
        for _ in range(self.n-1):
            for key in self.graph:
                for edge in self.graph[key]:
                    if dist[key] + edge[1] < dist[edge[0]]:
                        dist[edge[0]] = dist[key] + edge[1]
                        pred[edge[0]] = key

        for key in self.graph:
            for edge in self.graph[key]:
                if dist[key] + edge[1] < dist[edge[0]]:
                    raise ValueError('Graph contains a negative-weight cycle')
        
        return dist, pred
    
    def shortest_path(self, start: int, end: int):
        dist, prev = self.lazy(start=start, end=end)
        
        path: List[int] = []
        if (dist[end] == math.inf): return path
        
        at: int = end
        while at != None:
            path.append(at)
            at = prev[at]
        
        path.reverse()
        return path