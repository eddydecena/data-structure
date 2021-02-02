from collections import defaultdict

class Node():
    def __init__(self, label):
        self.label = label
        self.parent = self
        self.rank = 0

class UnionFind():
    def __init__(self, labels) -> None:
        self.nodes = [Node(label) for label in labels]
    
    def find(self, x) -> Node:
        root = x
        
        # find op
        while root.parent != root:
            root = root.parent
        
        # path compression
        while x.parent != root:
            parent = x.parent
            x.parent = root
            x = parent # Why
        
        return root
    
    def union(self, x, y) -> None:
        x = self.find(x)
        y = self.find(y)
        
        if x == y: return
        
        if x.rank > y.rank:
            y.parent = x
        elif y.rank > x.rank:
            x.parent = y
        elif x.rank == y.rank:
            y.parent = x.parent
            x.rank += 1
            
if __name__ == '__main__':
    uf = UnionFind('abcdefg')
    uf.union(uf.nodes[0], uf.nodes[1])
    uf.union(uf.nodes[0], uf.nodes[-1])
    r = uf.find(uf.nodes[0])
    print(f'{r.label} is the root node of {uf.nodes[-1].label}')