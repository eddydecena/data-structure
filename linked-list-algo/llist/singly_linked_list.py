from typing import Any
from typing import Optional
from typing import Callable

from llist.node import SinglyNode

class SinglyLinkedList():
    def __init__(self) -> None:
        self.size: int = 0
        self._head: Optional[SinglyNode] = None
        self._tail: Optional[SinglyNode] = None
    
    @property
    def head(self) -> SinglyNode:
        return self._head
    
    @head.setter
    def head(self, value: int) -> None:
        node: SinglyNode = SinglyNode(value)
        
        if self.size == 0:
            self._head = node
        else:
            _node = self.head
            
            while True:
                if _node.next == None:
                    _node.next = node
                    self._tail = node
                    break
                
                _node = _node.next
        
        self.size += 1
    
    @property
    def tail(self) -> SinglyNode:
        return self._tail
    
    def add_first(self, value: Any) -> None:
        node: SinglyNode = SinglyNode(value)
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