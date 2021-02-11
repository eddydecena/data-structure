from typing import Any
from typing import Optional

class Node():
    def __init__(self, key: str, value: Any, next: Optional[object] = None) -> None:
        self.key = key
        self.value = value
        self.next = next