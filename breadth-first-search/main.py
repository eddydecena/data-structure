from graph import bfs
from typing import Dict
from typing import List

GRAPH: Dict[str, List[str]] = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}

bfs(GRAPH)