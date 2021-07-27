class ButtomToTopMergeSort():
    @classmethod
    def mergesort(cls, array: list) -> list:
        low = 0
        high = len(array) - 1
        
        temp: list = array.copy()
        
        m: int = 1
        while m <= high - low:
            for i in range(low, high, 2*m):
                frm: int = i
                mid: int = i + m - 1
                to: int = min(i + 2*m - 1, high)
                cls.merge(array, temp, frm, mid, to)
            m: int = 2*m
    
    @staticmethod
    def merge(A: list, temp: int, frm: int, mid: int, to: int) ->  None:
        k: int = frm
        i: int = frm
        j: int = mid + 1
        
        while i <= mid and j <= to:
            if A[i] < A[j]:
                temp[k] = A[i]
                i = i + 1
            else:
                temp[k] = A[j]
                j = j + 1
            k = k + 1
        
        while i < len(A) and  i <= mid:
            temp[k] = A[i]
            k = k + 1
            i = i + 1
        
        for i in range(frm, to + 1):
            A[i] = temp[i]

if __name__ == '__main__':
    A = [5, 7, -9, 3, -4, 2, 8]

    print("Original array:", A)
    ButtomToTopMergeSort.mergesort(A)
    print("Sorted array:", A)


# # Merge two sorted sublists `A[frm…mid]` and `A[mid+1…to]`
# def merge(A, temp, frm, mid, to):
#     k = frm
#     i = frm
#     j = mid + 1

#     while i <= mid and j <= to:
#         if A[i] < A[j]:
#             temp[k] = A[i]
#             i = i + 1
#         else:
#             temp[k] = A[j]
#             j = j + 1
#         k = k + 1

#     while i < len(A) and i <= mid:
#         temp[k] = A[i]
#         k = k + 1
#         i = i + 1

#     for i in range(frm, to + 1):
#         A[i] = temp[i]

# def mergesort(A):
#     low = 0
#     high = len(A) - 1
 
#     # sort list `A` using a temporary list `temp`
#     temp = A.copy()
 
#     # divide the list into blocks of size `m`
#     # m = [1, 2, 4, 8, 16…]
 
#     m = 1
#     while m <= high - low:
 
#         # for m = 1, i = [0, 2, 4, 6, 8…]
#         # for m = 2, i = [0, 4, 8, 12…]
#         # for m = 4, i = [0, 8, 16…]
#         # …
 
#         for i in range(low, high, 2*m):
#             frm = i
#             mid = i + m - 1
#             to = min(i + 2*m - 1, high)
#             merge(A, temp, frm, mid, to)
 
#         m = 2*m
 
 
# # Iterative implementation of merge sort
# if __name__ == '__main__':
 
#     A = [5, 7, -9, 3, -4, 2, 8]
 
#     print("Original array:", A)
#     mergesort(A)
#     print("Modified array:", A)