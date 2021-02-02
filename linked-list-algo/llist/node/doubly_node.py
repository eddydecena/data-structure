# from typing import Any
# from typing import Union

# class DoublyNode():
#     def __init__(
#         self, value: Any,
#         prev: Union[int, None],
#         next: Union[int, None]) -> None:
        
#         self.value = value
#         self.next = next
#         self.prev = prev

from typing import Any
from typing import Optional

from llist.node import Node

class DoublyNode(Node):
    def __init__(self, value: Any) -> None:
        super(DoublyNode, self).__init__()
        
        self._value = value
        self._next = None
        self._prev = None
    
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
    def next(self, node: Optional[Node]=None) -> None:
        self._next = node
    
    @property
    def prev(self) -> None:
        return self._prev
    
    @prev.setter
    def prev(self, node: Optional[Node]=None):
        self._prev = node