from sort import Selection
from sort import Insertion
from sort import ShellSort
from sort import Shuffle

array: list = [10, 2, 3, 7, 1, 0]
print('Unordered array: ', array)

print(f'{"*" * 15} Selection sort {"*" * 15}')
print('Result: ', Selection.sort(array=array))

print(f'{"*" * 15} Insertion sort {"*" * 15}')
print('Result: ', Insertion.sort(array=array))

print(f'{"*" * 15} ShellSort sort {"*" * 15}')
print('Result: ', ShellSort.sort(array=array))

print(f'{"*" * 15} Shuffle sort {"*" * 15}')
print('Result: ', Shuffle.sort(array=array))