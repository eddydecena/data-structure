import random
from typing import List
from typing import Optional

class QuickFind():
    array: List[Optional[int]]
    
    def __init__(self, length: int) -> None:
        self.length = length
        self.array = list(range(0, length))
    
    def union(self, p: int, q: int) -> None:
        assert self.length == len(self.array), 'difference between array length and input length'
        
        pid = self.array[p]
        qid = self.array[q]
        
        for i in range(self.length):
            if self.array[i] == pid:
                self.array[i] = qid
    
    def connected(self, p: int, q: int) -> bool:
        return self.array[p] == self.array[q]

if __name__ == '__main__':
    num_op = 10   
    dc = QuickFind(num_op)
    for num in range(5):
        p = random.randint(0, num_op -1)
        q = random.randint(0, num_op-1)
        dc.union(p, q)
    dc.union(2, 5)
    print(dc.connected(2, 5))
    print('Test: ', dc.connected(3, 9))
    print(dc.array)