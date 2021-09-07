from typing import Dict
from typing import List

START: str = 'A'
GRAPH: Dict[str, List[str]] = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}

stack: list = []
visited: list = []

stack.append(START)
visited.append(START)

while len(stack) > 0:
    node = stack.pop()
    print(node, end=" ")
    
    for n in GRAPH[node]:
        if n not in visited:
            stack.append(n)
            visited.append(n)
