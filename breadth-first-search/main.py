from typing import Dict
from typing import List

from graph import bfs
from graph import has_path
from graph import connected
from graph import KrushalAlgo
from graph import LazyPrims
from graph import LazyDijkstras

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

ka = LazyDijkstras(6)
ka.add_edge(0, 1, 4)
ka.add_edge(0, 2, 4)
ka.add_edge(1, 2, 2)
ka.add_edge(1, 0, 4)
ka.add_edge(2, 0, 4)
ka.add_edge(2, 1, 2)
ka.add_edge(2, 3, 3)
ka.add_edge(2, 4, 1)
ka.add_edge(2, 5, 6)
ka.add_edge(3, 2, 3)
ka.add_edge(3, 5, 2)
ka.add_edge(5, 2, 6)
ka.add_edge(5, 3, 2)
ka.add_edge(5, 4, 3)
ka.add_edge(4, 2, 1)
ka.add_edge(4, 5, 3)
print(ka.run(start=0, end=5, early_stop=True))