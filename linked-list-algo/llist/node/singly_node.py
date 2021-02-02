from typing import Any
from typing import Optional

from llist.node import Node

class SinglyNode(Node):
    def __init__(
        self, 
        value: Any, 
        next: Optional[Node] = None) -> None:
        
        super(SinglyNode, self).__init__()
        
        self._value = value
        self._next = next
    
    @property
    def value(self) -> Any:
        return self._value
    
    @value.setter
    def value(self, v: Any) -> None:
        self._value = v

    @property
    def next(self) -> Node:
        return self._next
    
    @next.setter
    def next(self, node=Node) -> None:
        self._next = node