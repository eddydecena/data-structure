from typing import Dict
from typing import List
from typing import Tuple
from typing import Union

def bfs(GRAPH: Dict[str, List[str]], start: str='A', end: str='F', shortest_path: bool=False) -> Union[List[str], int]:
    queue: List[Tuple[str, int]] = []
    visited: List[str] = []

    queue.append((start, 0))
    visited.append(start)

    while len(queue) > 0:
        node: str = queue.pop(0)
        print(node[0], end=" ")
        
        if (node[0] == end) and shortest_path:
            return node[1]
            
        for neighbour in GRAPH[node[0]]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append((neighbour, node[1] + 1))
    
    return visited