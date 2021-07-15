import random
from typing import List
from typing import Optional

class QuickUnion():
    array: List[Optional[int]]
    
    def __init__(self, length: int) -> None:
        self.length = length
        self.array = list(range(0, length))
    
    def root(self, i: int) -> int:
        while(self.array[i] != i):
            # i = self.array[self.array[i]]
            self.array[i] = self.array[self.array[1]]
            i  = self.array[1]
        
        return i
    
    def union(self, p: int, q: int) -> None:
        assert self.length == len(self.array), 'difference between array length and input length'
        
        i: int = self.root(p)
        j: int = self.root(q)
        self.array[i] = j
    
    def connected(self, p: int, q: int) -> bool:
        return self.root(p) == self.root(q)

if __name__ == '__main__':
    num_op = 10   
    dc = QuickUnion(num_op)
    for num in range(5):
        p = random.randint(0, num_op -1)
        q = random.randint(0, num_op-1)
        dc.union(p, q)
    dc.union(2, 5)
    print(dc.connected(2, 5))
    print('Test: ', dc.connected(3, 9))
    print(dc.array)