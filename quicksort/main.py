class QuickSort():
    @classmethod
    def sort(cls, array: list, low: int, high: int) -> list:
        if len(array) <= 1:
            return array
        
        if low < high:
            pi: int = cls.partition(array, low, high)
            
            cls.sort(array, low, pi-1)
            cls.sort(array, pi + 1, high)

    @staticmethod
    def partition(array: list, low: int, high: int) ->  None:
        i: int = (low-1) # why subtract by -1
        
        pivot: int = array[high]
        
        for j in range(low, high):
            if array[j] <= pivot:
                i = i+1
                
                array[i], array[j] = array[j], array[i]
        
        array[i+1], array[high] = array[high], array[i+1]
        return (i+1)

if __name__ == '__main__':
    A = [5, 7, -9, 3, -4, 2, 8]

    print("Original array:", A)
    QuickSort.sort(A, 0, len(A)-1)
    print("Sorted array:", A)