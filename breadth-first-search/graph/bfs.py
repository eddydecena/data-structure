from typing import Dict
from typing import List
from typing import Any

def bfs(GRAPH: Dict[str, List[str]]) -> Any:
    queue: List[str] = []
    visited: List[str] = []

    queue.append('A')
    visited.append('A')

    while len(queue) > 0:
        node: str = queue.pop(0)
        print(node, end=" ")
        
        for neighbour in GRAPH[node]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)