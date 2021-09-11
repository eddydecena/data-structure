from typing import Dict
from typing import List

from . import bfs

def connected(GRAPH: Dict[str, List[str]]):
    visited: List[str] = []
    count: int = 0
    
    for key in GRAPH:
        if key not in visited:
            count += 1
        
        visited_bfs = bfs(GRAPH, start=key)
        visited = list(set(visited) | set(visited_bfs))
    
    return count