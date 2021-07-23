import random

class Shuffle():
    @classmethod
    def sort(cls, array: list) -> list:
        for i in range(0, len(array)):
            r: int = random.randint(0, i)
            cls.swap(array, i, r)
        return array
    
    @staticmethod
    def swap(array: list, i: int, min: int):
        temp = array[i]
        array[i] = array[min]
        array[min] = temp
        return array