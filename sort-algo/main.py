from sort import Selection
from sort import Insertion
from sort import ShellSort

array: list = [10, 2, 3, 7, 1, 0]
print('Unordered array: ', array)

print(f'{"*" * 15} Selection sort {"*" * 15}')
print('Result: ', Selection.sort(array=[10, 2, 3, 7, 1, 0]))

print(f'{"*" * 15} Insertion sort {"*" * 15}')
print('Result: ', Insertion.sort(array=[10, 2, 3, 7, 1, 0]))

print(f'{"*" * 15} ShellSort sort {"*" * 15}')
print('Result: ', ShellSort.sort(array=[10, 2, 3, 7, 1, 0]))