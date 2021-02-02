from typing import Union
from collections import deque

def bracketReverse(bracket: str) -> Union[str, None]:
    open_list = ['(', '{', '[']
    close_list = [')', '}', ']']
    
    try:
        index = close_list.index(bracket)
        return open_list[index]
    except ValueError:
        return None

def bracketCheck(brackets: str) -> bool:
    stack = deque()
    
    for bracket in brackets:
        try:
            if stack[-1] == bracketReverse(bracket):
                stack.pop()
            else:
                stack.append(bracket)
        except IndexError:
            stack.append(bracket)
    
    return len(stack) == 0

if __name__ == '__main__':
    string = '{{[[(())]]}}'
    results: bool = bracketCheck(string)
    
    if results:
        print('Not lint for bracket')
    else:
        print('Some lint for bracket')
