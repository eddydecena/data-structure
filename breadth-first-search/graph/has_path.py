from typing import Dict
from typing import List

from . import bfs

def has_path(GRAPH: Dict[str, List[str]], source: str, destination: str):
    visited = bfs(GRAPH, source)
    if destination in visited:
        return True
    
    return False