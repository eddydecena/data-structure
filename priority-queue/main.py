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

if __name__ == '__main__':
    pq: PriorityQueue = PriorityQueue()
    pq.insert(8)
    pq.insert(12)
    pq.insert(10)
    pq.insert(9)
    pq.insert(11)
    pq.insert(20)
    pq.insert(15)
    pq.insert(5)
    print(pq.queue)
    print(pq.delete_max())
    print(pq.queue)