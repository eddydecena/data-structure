class Selection():
    @classmethod
    def sort(cls, array: list) -> list:
        for i in range(len(array)):
            min: int = i
            for j in range(i, len(array)):
                if cls.less(array[j], array[i]):
                    min = j
            array = cls.swap(array, i, min)
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