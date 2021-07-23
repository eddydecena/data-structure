class Insertion():
    @classmethod
    def sort(cls, array: list) -> list:
        for i in range(len(array)+1):
            for j in reversed(range(1, i)):
                if cls.less(array[j], array[j-1]):
                    array = cls.swap(array, j, j-1)
                else:
                    break
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