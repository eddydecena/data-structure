GRAPH = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}

queue = []
visited = []

queue.append('A')
visited.append('A')

while len(queue) > 0:
    node = queue.pop(0)
    print(node, end=" ")
    
    for neighbour in GRAPH[node]:
        if neighbour not in visited:
            visited.append(neighbour)
            queue.append(neighbour)
