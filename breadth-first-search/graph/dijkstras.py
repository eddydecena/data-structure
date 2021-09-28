from typing import List
from typing import Tuple
from typing import Dict
from typing import Optional
from queue import PriorityQueue
import heapq
import math

class Dijkstras():
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
    
    def lazy(self, start: int = 0, end: Optional[int]=None, early_stop: Optional[bool]=False) -> Tuple[List[int], List[int]]:
        dist: List[int] = [math.inf] * self.n
        prev: List[int] = [None] * self.n
        
        dist[start] = 0
        
        self.pq.put((start, 0))
        
        while not self.pq.empty():
            index, min_value = self.pq.get()
            self.visited[index] = True
            if dist[index] < min_value: continue
            for edge in self.graph[index]:
                if self.visited[edge[0]]: continue
                    
                new_dist = dist[index] + edge[1]
                
                if new_dist < dist[edge[0]]:
                    prev[edge[0]] = index
                    dist[edge[0]] = new_dist
                    self.pq.put((edge[0], new_dist))
            if early_stop and (index == end):
                return dist[end]

    def eager(self, start: int = 0, end: Optional[int]=None, early_stop: Optional[bool]=False):
        dist: List[int] = [math.inf] * self.n
        prev: List[int] = [None] * self.n
        
        dist[start] = 0

        heapq.heappush(self.ipq, (start, start))
        
        while len(self.ipq) > 0:
            index, min_value = heapq.heappop(self.ipq)
            self.visited[index] = True
            if dist[index] < min_value: continue
            for edge in self.graph[index]:
                if self.visited[edge[0]]: continue
                    
                new_dist = dist[index] + edge[1]
                
                if new_dist < dist[edge[0]]:
                    prev[edge[0]] = index
                    dist[edge[0]] = new_dist
                    if not edge[0] in self.ipq:
                        heapq.heappush(self.ipq, (edge[0], new_dist))
                    else:
                        heapq.heapreplace(self.ipq, (edge[0], new_dist))
            if early_stop and (index == end):
                return dist[end]
    
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