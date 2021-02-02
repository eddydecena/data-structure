from typing import Optional
from typing import Any

from bts.node import Node

class BinaryTreeSearch():
    def __init__(self, arr: list) -> None:
        self._tree: Optional[Node] = None
        
        for value in arr:
            self.add(value)
    
    @property
    def tree(self) -> Node:
        return self._tree
    
    def search_recursively(self, value: Any, tree: Optional[Node] == None) -> None:
        if tree == None and tree.value == value:
            return tree
        elif value < tree.value:
            self.search_recursively(value, tree.left)
        elif value > tree.value:
            self.search_recursively(value, tree.right)
    
    def search_iteratively(self, value: Any) -> None:
        current_node = self._tree
        
        while current_node != None:
            if value == current_node.value:
                return current_node
            elif value < current_node.value:
                current_node = current_node.left
            elif value > current_node.value:
                current_node = current_node.right
        return current_node
    
    def add(self, value: Any) -> None:
        node = Node(value)
        current_node = self._tree
        
        while True:
            if current_node == None:
                self._tree = node
                break
            elif node.value < current_node.value:
                if not current_node.left:
                    current_node.left = node
                    break
                current_node = current_node.left
            elif node.value > current_node.value:
                if not current_node.right:
                    current_node.right = node
                    break
                current_node = current_node.right