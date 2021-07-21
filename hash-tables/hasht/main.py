from typing import Optional
from typing import Any

from hasht.node import Node

class HashTable():
    def __init__(self, capacity: int = 100) -> None:
        self.size: int = 0
        self._capacity = capacity
        self.buckets: list[Optional[Node]] = [None] * self._capacity
        self.load_factor = 0.7
        self.threshold = self._capacity * self.load_factor
    
    def hash(self, key) -> int:
        hashsum = 0
        
        for idx, c in enumerate(key):
            hashsum = (idx + len(key)) ** ord(c)
            hashsum = hashsum % self._capacity
        
        return hashsum
    
    def insert(self, key: str, value: Any) -> None:
        index = self.hash(key)
        
        node = self.buckets[index]
        
        if node is None:
            self.buckets[index] = Node(key, value)
            return

        while True:
            if node.next is None:
                node.next = Node(key, value)
                break
            
            node = node.next
        
        self.size += 1
        
        if self.size >= self.threshold:
            self.resize(2 * self._capacity + 1)
    
    def retrive(self, key: str) -> Any:
        index = self.hash(key)
        
        node = self.buckets[index]
        
        while ((node is not None) and (node.key != key)):
            node = node.next
        
        if node == None:
            return None
        else:
            return node
    
    def remove(self, key: str):
        index = self.hash(key)
        
        node = self.buckets[index]
        
        if node.key == key:
            self.buckets[index] = node.next
            return
        
        prev = node
        while ((node is not None) and (node.key != key)):
            if (node.next is not None):
                break
            
            prev = node
            node = node.next
        
        node.next = prev.next.next
    
    def resize(self, new_capacity: int):
        temp: HashTable = HashTable(new_capacity)
        
        for node in self.buckets:
            while node:
                temp.insert(node.key, node.value)
                node = node.next
        
        self.buckets = temp.buckets
        self._capacity = temp._capacity
        self.threshold = self._capacity * self.load_factor