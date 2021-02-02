from typing import Any
from typing import Optional
from typing import Callable

from llist.node import DoublyNode

class DoublyLinkedList():
    def __init__(self) -> None:
        self.size: int = 0
        self._head: Optional[DoublyNode] = None
        self._tail: Optional[DoublyNode] = None
    
    @property
    def head(self) -> DoublyNode:
        return self._head
    
    @head.setter
    def head(self, value: int) -> None:
        node: DoublyNode = DoublyNode(value)
        
        if self.size == 0:
            self._head = node
        else:
            _node = self.head
            
            while True:
                if _node.next == None:
                    node.prev = _node
                    _node.next = node
                    self._tail = node
                    break
                
                _node = _node.next
        
        self.size += 1
    
    @property
    def tail(self) -> DoublyNode:
        return self._tail
    
    def add_first(self, value: Any) -> None:
        node: DoublyNode = DoublyNode(value)
        self._head.prev = node
        node.next = self._head
        self._head = node
        self.size += 1
    
    def delete_last(self):
        __node = self._head
        _node = __node
        
        while True:
            if _node.next == None:
                __node.next = None
                break
            
            __node = _node
            _node = _node.next
        
        self._tail = __node
        self.size -= 1
    
    def map(self, fn: Callable[[Any], Any]) -> None:
        node = self._head
        
        while node is not None:
            node.value = fn(node.value)
            node = node.next