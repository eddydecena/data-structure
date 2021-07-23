from typing import List

class ShellSort():
    @classmethod
    def sort(cls, array: list) -> list:
        n: int = len(array)
        gaps: List[int] = [701, 301, 132, 57, 23, 10, 4, 1]
        
        for gap in gaps:
            for i in range(gap, n):
                temp = array[i]
                j: int = i
                while j >= gap and cls.less(array[j], array[j-gap]):
                    array = cls.swap(array, j, j-gap)
                    j -= gap
                array[j] = temp
        return array
        
    @staticmethod
    def less(x: int, y: int):
        if x < y:
            return True
        return False
    
    @staticmethod
    def swap(array: list, i: int, min: int):
        temp = array[i]
        array[i] = array[min]
        array[min] = temp
        return array