from typing import Dict
from typing import List

def bfs(GRAPH: Dict[str, List[str]], start: str='A') -> List[str]:
    queue: List[str] = []
    visited: List[str] = []

    queue.append(start)
    visited.append(start)

    while len(queue) > 0:
        node: str = queue.pop(0)
        print(node, end=" ")
        
        for neighbour in GRAPH[node]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
    
    return visited