class PriorityQueue():
    queue: list
    
    def __init__(self) -> None:
        self.queue = []
    
    def isEmpty(self) -> bool:
        return len(self.queue) == 0
    
    def insert(self, data) -> None:
        self.queue.append(data)
    
    def delete_max(self):
        try:
            max: int = 0
            for i, value in enumerate(self.queue):
                if value > self.queue[max]:
                    max = i
            item = self.queue[max]
            del self.queue[max]
            return item
        except IndexError:
            print()
            exit()

class BinaryHeapPQ():
    heap: list
    N: int
    
    def __init__(self, capacity: int) -> None:
        self.heap = [None] * (capacity + 1)
        self.N = 0
    
    def insert(self, data) -> None:
        self.N += 1
        self.heap[self.N] = data
        self.swim(self.N)
        # print(self.heap)
    
    def delete_max(self) -> None:
        pass
    
    def swim(self, k: int):
        # print(k, self.heap[k//2], self.heap[k], self.less(k//2, k))
        while (k > 1) and self.less(k//2, k):
            self.swap(k//2, k)
            k //= 2
            print(k)
    
    def less(self, x: int, y: int):
        if self.heap[x] < self.heap[y]:
            return True
        return False

    def swap(self, i: int, min: int):
        temp = self.heap[i]
        self.heap[i] = self.heap[min]
        self.heap[min] = temp

if __name__ == '__main__':
    pq: BinaryHeapPQ = BinaryHeapPQ(10)
    pq.insert(15)
    pq.insert(12)
    pq.insert(10)
    pq.insert(11)
    pq.insert(20)
    pq.insert(11)
    print(pq.heap)
    # print(pq.delete_max())
    # print(pq.queue)