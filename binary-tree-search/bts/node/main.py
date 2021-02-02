from typing import Any
from typing import Optional

class Node():
    def __init__(self, value: Any, left: Optional[object] = None, right: Optional[object] = None):
        self.value = value
        self.left = left
        self.right = right
    
    def is_leaf(self) -> bool:
        if self.left == None and self.right == None:
            return True
        
        return False