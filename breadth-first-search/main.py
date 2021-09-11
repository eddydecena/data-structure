from typing import Dict
from typing import List

from graph import bfs
from graph import has_path
from graph import connected

# GRAPH: Dict[str, List[str]] = {
#     'A' : ['B','C'],
#     'B' : ['D', 'E'],
#     'C' : ['F'],
#     'D' : [],
#     'E' : ['F'],
#     'F' : []
# }

GRAPH: Dict[str, List[str]] = {
    'A' : ['B','C'],
    'B' : ['A', 'D', 'E'],
    'C' : ['A', 'F'],
    'D' : ['B'],
    'E' : ['B', 'F'],
    'F' : ['C', 'E'],
    'G' : ['H', 'I'],
    'H' : ['G', 'J', 'K'],
    'I' : ['G', 'L'],
    'J' : ['H'],
    'K' : ['H', 'L'],
    'L' : ['K', 'I'],
    'Z' : []
}

print(connected(GRAPH))